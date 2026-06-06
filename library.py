class Book:
    def __init__(self, title, author):
        self.title = (self, title, author)
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}', has been borrowed.")
        else:
            print(f"'{self.title}', is already borrowed come back later...")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}', has been returned.")
        else:
            print(f"'{self.title}', isn't borrowed yet.")

book1 = Book("Goosebumps", "RL.STINE")
book2 = Book("Rezero", "Tapei")
book3 = Book("Help wanted", "Unknown")

book1.borrow()
book2.borrow()
book3.borrow()

print()
book1.return_book()
book2.return_book()

print()
book2.borrow()
book3.return_book