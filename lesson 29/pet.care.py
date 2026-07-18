# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Pet Care Reminder")
root.geometry("300x200")

# Function to show a message box
def feed_pet():
    messagebox.showinfo("Reminder", "Your pet has been fed!")

# Event handler when mouse enters the button
def mouse_enter(event):
    status.config(text="Click the button to feed your pet.")

# Event handler when mouse leave the button
def mouse_leave(event):
    status.config(text="")

# Create button 
button = Button(root, text="Feed Pet", command=feed_pet)
button.pack(pady=40)

# Bind mouse events to the button
button.bind("<Enter>", mouse_enter)
button.bind("<Leave>", mouse_leave)

# Label to display messages
status = Label(root, text="", fg="blue")
status.pack()

# Start the appilication
root.mainloop()