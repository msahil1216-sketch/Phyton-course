from tkinter import *

def calculate():

    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        si = (principal * rate * time) / 100

        ci = principal * (1 + rate/100) ** time - principal

        result.config(
            text=f"Simple Interest = {si:.2f}\nCompound Interest = {ci:.2f}"
        )

    except:
        result.config(text="Please enter valid numbers.")

root = Tk()

root.title("Interest Calculator App")
root.geometry("400x400")

Label(root,
      text="Interest Calculator",
      font=("Arial",16,"bold")).grid(row=0,column=0,columnspan=2,pady=20)

Label(root,text="Principal").grid(row=1,column=0,padx=10,pady=5)
principal_entry = Entry(root)
principal_entry.grid(row=1,column=1)

Label(root,text="Time (Years)").grid(row=2,column=0,padx=10,pady=5)
time_entry = Entry(root)
time_entry.grid(row=2,column=1)

Label(root,text="Rate (%)").grid(row=3,column=0,padx=10,pady=5)
rate_entry = Entry(root)
rate_entry.grid(row=3,column=1)

Button(root,
       text="Calculate",
       command=calculate,
       bg="green",
       fg="white").grid(row=4,column=0,columnspan=2,pady=20)

result = Label(root,text="",font=("Arial",12))
result.grid(row=5,column=0,columnspan=2)

root.mainloop()