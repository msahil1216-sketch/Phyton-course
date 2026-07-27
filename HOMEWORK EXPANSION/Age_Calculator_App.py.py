from tkinter import *
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result.config(text=f"Hello {name}!\nYour present age is {age} years.")

    except:
        messagebox.showerror("Error", "Please enter valid information.")

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

Label(root, text="Age Calculator App",
      font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5, sticky="w")
name_entry = Entry(root, width=25)
name_entry.grid(row=1, column=1)

Label(root, text="Date").grid(row=2, column=0, padx=10, pady=5, sticky="w")
day_entry = Entry(root, width=25)
day_entry.grid(row=2, column=1)

Label(root, text="Month").grid(row=3, column=0, padx=10, pady=5, sticky="w")
month_entry = Entry(root, width=25)
month_entry.grid(row=3, column=1)

Label(root, text="Year").grid(row=4, column=0, padx=10, pady=5, sticky="w")
year_entry = Entry(root, width=25)
year_entry.grid(row=4, column=1)

Button(root, text="Calculate Age",
       command=calculate_age,
       bg="green",
       fg="white").grid(row=5, column=0, columnspan=2, pady=20)

result = Label(root, text="", font=("Arial", 12))
result.grid(row=6, column=0, columnspan=2)

root.mainloop()