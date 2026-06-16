import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("350x300")

        self.best_score = None
        self.ranges = {"Easy": 10, "Medium": 50, "Hard": 100}

        tk.Label(root, text="Select Difficulty").pack()

        self.difficulty = tk.StringVar(value="Easy")
        for level in self.ranges:
            tk.Radiobutton(root, text=f"{level} (1-{self.ranges[level]})",
                           variable=self.difficulty, value=level).pack()

        tk.Button(root, text="New Game", command=self.start_game).pack(pady=5)

        self.info = tk.Label(root)
        self.info.pack()

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.guess_btn = tk.Button(root, text="Guess",
                                   command=self.check_guess, state="disabled")
        self.guess_btn.pack()

        self.result = tk.Label(root)
        self.result.pack(pady=5)

        self.attempts_lbl = tk.Label(root, text="Attempts: 0")
        self.attempts_lbl.pack()

        self.best_lbl = tk.Label(root, text="Best Score: None")
        self.best_lbl.pack()

    def start_game(self):
        self.high = self.ranges[self.difficulty.get()]
        self.secret = random.randint(1, self.high)
        self.attempts = 0

        self.info.config(text=f"Guess a number between 1 and {self.high}")
        self.result.config(text="")
        self.attempts_lbl.config(text="Attempts: 0")
        self.entry.delete(0, tk.END)
        self.guess_btn.config(state="normal")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            self.attempts_lbl.config(text=f"Attempts: {self.attempts}")

            if guess < self.secret:
                self.result.config(text="Too Low , Bada Chuno ⬆", fg="blue")
            elif guess > self.secret:
                self.result.config(text="Too High , Chota Chuno ⬇", fg="orange")
            else:
                self.result.config(text="Shi hai! 🎉", fg="green")

                if self.best_score is None or self.attempts < self.best_score:
                    self.best_score = self.attempts
                    self.best_lbl.config(text=f"Best Score: {self.best_score}")

                messagebox.showinfo("Win", f"Guessed in {self.attempts} attempts!")
                self.guess_btn.config(state="disabled")

            self.entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Enter a valid number!")

root = tk.Tk()
NumberGuessingGame(root)
root.mainloop()