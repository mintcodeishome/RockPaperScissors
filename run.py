import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        # Initialize scores
        self.user_wins = 0
        self.computer_wins = 0
        self.draws = 0

        # Load and resize images
        self.rock_img = self.load_and_resize_image("rock.png", (100, 100))
        self.paper_img = self.load_and_resize_image("paper.png", (100, 100))
        self.scissors_img = self.load_and_resize_image("scissors.png", (100, 100))

        # Set background color
        self.root.configure(bg='#F4F4F4')

        # Create labels
        self.label_instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14), bg='#F4F4F4')
        self.label_result = tk.Label(root, text="", font=("Helvetica", 12), fg="blue", bg='#F4F4F4')
        self.label_scores = tk.Label(root, text="Wins: 0  Losses: 0  Draws: 0", font=("Helvetica", 12), fg="green", bg='#F4F4F4')

        # Create buttons with background color and hover effect
        button_styles = {'bg': '#4CAF50', 'activebackground': '#45a049'}
        self.button_rock = tk.Button(root, image=self.rock_img, command=lambda: self.play("rock"), **button_styles)
        self.button_paper = tk.Button(root, image=self.paper_img, command=lambda: self.play("paper"), **button_styles)
        self.button_scissors = tk.Button(root, image=self.scissors_img, command=lambda: self.play("scissors"), **button_styles)
        self.button_reset = tk.Button(root, text="Reset", command=self.ask_play_again, bg='#008CBA', fg='white', font=('Helvetica', 10))

        # Create labels for user and computer choices
        self.label_user_choice = tk.Label(root, text="Your choice: ", font=("Helvetica", 12), bg='#F4F4F4')
        self.label_computer_choice = tk.Label(root, text="Computer's choice: ", font=("Helvetica", 12), bg='#F4F4F4')

        # Pack widgets
        self.label_instruction.grid(row=0, column=0, columnspan=3, pady=10)
        self.button_rock.grid(row=1, column=0, padx=20)
        self.button_paper.grid(row=1, column=1, padx=20)
        self.button_scissors.grid(row=1, column=2, padx=20)
        self.label_user_choice.grid(row=2, column=0, columnspan=3, pady=5)
        self.label_computer_choice.grid(row=3, column=0, columnspan=3, pady=5)
        self.label_result.grid(row=4, column=0, columnspan=3, pady=10)
        self.label_scores.grid(row=5, column=0, columnspan=2, pady=5)
        self.button_reset.grid(row=5, column=2, pady=5)

    def load_and_resize_image(self, filename, size):
        img = Image.open(filename)
        img = img.resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def play(self, user_choice):
        # Choices for the computer
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Visual effect for user's selection
        self.visual_effect(self.get_button_by_choice(user_choice))

        # Determine the winner
        winner = self.determine_winner(user_choice, computer_choice)

        # Visual effect for computer's selection (slight delay for a more dynamic feel)
        self.root.after(1000, lambda: self.visual_effect(self.get_button_by_choice(computer_choice)))

        # Update labels for user and computer choices
        self.label_user_choice.config(text=f"Your choice: {user_choice.capitalize()}")
        self.label_computer_choice.config(text=f"Computer's choice: {computer_choice.capitalize()}")

        # Update scores
        if winner == "user":
            self.user_wins += 1
        elif winner == "computer":
            self.computer_wins += 1
        else:
            self.draws += 1

        # Display result and update scores
        if winner == "draw":
            result_text = "It's a Draw!"
        else:
            result_text = f"{winner.capitalize()} wins!"

        self.label_result.config(text=result_text)
        self.label_scores.config(text=f"Wins: {self.user_wins}  Losses: {self.computer_wins}  Draws: {self.draws}")

    def ask_play_again(self):
        # Ask if the user wants to play again
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            # Reset labels and scores for a new round
            self.label_result.config(text="")
            self.label_user_choice.config(text="Your choice: ")
            self.label_computer_choice.config(text="Computer's choice: ")

            # Reset scores to zero
            self.user_wins = 0
            self.computer_wins = 0
            self.draws = 0
            self.label_scores.config(text="Wins: 0  Losses: 0  Draws: 0")
        else:
            self.reset_game()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            return "user"
        else:
            return "computer"

    def reset_game(self):
        # Reset scores
        self.user_wins = 0
        self.computer_wins = 0
        self.draws = 0

        # Update labels
        self.label_scores.config(text="Wins: 0  Losses: 0  Draws: 0")
        self.label_result.config(text="")
        self.label_user_choice.config(text="Your choice: ")
        self.label_computer_choice.config(text="Computer's choice: ")

    def get_button_by_choice(self, choice):
        if choice == "rock":
            return self.button_rock
        elif choice == "paper":
            return self.button_paper
        elif choice == "scissors":
            return self.button_scissors

    def visual_effect(self, button):
        # Visual effect - change background color temporarily
        original_bg = button.cget('bg')
        button.configure(bg='#FFD700')  # Change to gold color
        self.root.after(500, lambda: button.configure(bg=original_bg))  # Change back to original color after 500 milliseconds


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
