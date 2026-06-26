                      # File Organizer Script Made By :- SHARAD SHARMA
            #TASK-2: File Organizer Script USING PYTHON COMPLETED ON 26-06-2024
                           # BY Syntecxhub Technologies Pvt. Ltd.       



import os
import shutil

# Here, we are taking the path of the directory from the user and then listing all the files in that directory. After that, we are iterating through each file and checking its extension. If a folder with that extension already exists, we move the file into that folder. If it doesn't exist, we create a new folder with that extension and then move the file into it.

path = input("Enter the path of the directory to organize: ")
files = os.listdir(path)

# Here, we are iterating through each file in the directory and checking its extension. If a folder with that extension already exists, we move the file into that folder. If it doesn't exist, we create a new folder with that extension and then move the file into it.

for file in files:
    filename,extension = os.path.splitext(file)
    extension=extension[1:]
   
   # Here, we are checking if the extension is empty or not. If it is empty, we are moving the file to a folder named 'Others'. If it is not empty, we are checking if a folder with that extension already exists. If it does, we move the file into that folder. If it doesn't, we create a new folder with that extension and then move the file into it.
    
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    
# Here, we are printing a message to the user indicating that the directory has been successfully organized.    
    
print("Directory successfully organized!")    