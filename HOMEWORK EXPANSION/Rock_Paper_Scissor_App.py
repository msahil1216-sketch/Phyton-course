from tkinter import *
import random

def play(user_choice):

    choices = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"

    else:
        result = "Computer Wins!"

    output.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}\n\n{result}"
    )

root = Tk()

root.title("Rock Paper Scissor App")
root.geometry("400x400")

Label(root,
      text="Rock Paper Scissor",
      font=("Arial",16,"bold")).pack(pady=20)

Button(root,
       text="Rock",
       width=15,
       command=lambda: play("Rock")).pack(pady=5)

Button(root,
       text="Paper",
       width=15,
       command=lambda: play("Paper")).pack(pady=5)

Button(root,
       text="Scissors",
       width=15,
       command=lambda: play("Scissors")).pack(pady=5)

output = Label(root,
               text="Choose one option",
               font=("Arial",12))

output.pack(pady=30)

root.mainloop()