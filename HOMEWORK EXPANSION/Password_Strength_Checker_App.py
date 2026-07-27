from tkinter import *

def check_password():

    password = password_entry.get()

    length = len(password)

    if length <= 5:
        result.config(text="Weak", fg="red")

    elif length <= 8:
        result.config(text="Medium", fg="yellow")

    elif length <= 12:
        result.config(text="Strong", fg="light green")

    else:
        result.config(text="Very Strong", fg="dark green")

root = Tk()

root.title("Password Strength Checker App")
root.geometry("400x400")

Label(root,
      text="Password Strength Checker",
      font=("Arial",16,"bold")).pack(pady=20)

Label(root,text="Enter Password").pack()

password_entry = Entry(root,width=25,show="*")
password_entry.pack(pady=10)

Button(root,
       text="Check Strength",
       command=check_password,
       bg="blue",
       fg="white").pack(pady=20)

result = Label(root,
               text="",
               font=("Arial",14,"bold"))
result.pack()

root.mainloop()