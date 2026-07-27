from tkinter import *

def convert():

    try:
        inches = float(inch_entry.get())

        centimeters = inches * 2.54

        result.config(
            text=f"{inches} inches = {centimeters:.2f} cm"
        )

    except:
        result.config(text="Please enter a valid number.")

root = Tk()

root.title("Length Converter App")
root.geometry("400x400")

Label(root,
      text="Length Converter",
      font=("Arial",16,"bold")).pack(pady=20)

Label(root,text="Enter Inches").pack()

inch_entry = Entry(root,width=20)
inch_entry.pack(pady=10)

Button(root,
       text="Convert",
       command=convert,
       bg="green",
       fg="white").pack(pady=20)

result = Label(root,
               text="",
               font=("Arial",12))
result.pack()

root.mainloop()