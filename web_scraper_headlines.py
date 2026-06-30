import os
import requests
from bs4 import BeautifulSoup

URL = "https://news.google.com/rss"

try:
    # Download RSS feed
    response = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )
    response.raise_for_status()

    # Parse XML
    soup = BeautifulSoup(response.content, "xml")

    news_items = []

    for item in soup.find_all("item"):
        title = item.title.get_text(strip=True) if item.title else "No Title"
        link = item.link.get_text(strip=True) if item.link else "#"
        pub_date = item.pubDate.get_text(strip=True) if item.pubDate else "No Date"

        news_items.append({
            "title": title,
            "link": link,
            "date": pub_date
        })

    # HTML header
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Google News Headlines</title>

<style>
body{
    font-family: Arial, sans-serif;
    background:#f4f4f4;
    margin:40px;
}

h1{
    color:#bb1919;
    text-align:center;
}

.news{
    background:white;
    padding:15px;
    margin-bottom:20px;
    border-radius:8px;
    box-shadow:0 2px 8px rgba(0,0,0,0.15);
}

.title{
    font-size:22px;
    font-weight:bold;
}

.date{
    color:#666;
    margin-top:8px;
}

a{
    color:#0056b3;
    text-decoration:none;
}

a:hover{
    text-decoration:underline;
}
</style>

</head>
<body>

<h1>Google News Headlines</h1>
"""

    # Add news items
    for news in news_items:
        html += f"""
<div class="news">
    <div class="title">
        <a href="{news['link']}" target="_blank">
            {news['title']}
        </a>
    </div>

    <div class="date">
        <strong>Date:</strong> {news['date']}
    </div>

    <div>
        <strong>Link:</strong>
        <a href="{news['link']}" target="_blank">
            {news['link']}
        </a>
    </div>
</div>
"""

    html += """
</body>
</html>
"""

    # Save file
    output_file = os.path.abspath("news.html")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully saved {len(news_items)} news articles.")
    print("HTML file created successfully!")
    print("Location:", output_file)

except requests.exceptions.RequestException as e:
    print("Network Error:")
    print(e)

except Exception as e:
    print("Unexpected Error:")
    print(e)