from tkinter import *

def calculate():

    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        product = num1 * num2

        result.delete("1.0", END)
        result.insert(END, product)

    except:
        result.delete("1.0", END)
        result.insert(END, "Invalid Input")


root = Tk()

root.title("Getting Started with Widgets")
root.geometry("400x300")

Label(root, text="Enter two numbers to calculate their product").pack(pady=10)

Label(root, text="First Number").pack()
entry1 = Entry(root)
entry1.pack()

Label(root, text="Second Number").pack()
entry2 = Entry(root)
entry2.pack()

Button(root,
       text="Calculate Product",
       command=calculate).pack(pady=10)

result = Text(root, height=2, width=20)
result.pack()

root.mainloop()