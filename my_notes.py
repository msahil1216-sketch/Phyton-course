from tkinter import *
from tkinter.filedialog import askopenfilename, asksavefilename

# Create window
root = Tk()
root.title("Mini Notes")
root.geometry("500x350")

# Open File Function
def open_note():
    file = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file:
        text_box.delete(1.0, END)
        with open(file, "r") as f:
            text_box.insert(END, f.read())

def save_note():
    file = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file:
        with open(file, "w") as f:
            f.write(text_box.get(1.0, END))

toolbar = Frame(root, bg="lightblue")
toolbar.pack(fill=x)

Button(toolbar, text="Open", command=open_note).pack(side=LEFT. padx=5, pady=5)
Button(toolbar, text="Save", command=save_note).pack(side=LEFT. padx=5, pady=5)

text_box = Text(root, font=("Arial, 12"), wrap=WORD)
text_box.pack(fill=BOTH, expand=True, padx=10, pady=10)

root.mainloop()