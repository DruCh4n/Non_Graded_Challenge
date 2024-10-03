class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Title : {self.title}, Author : {self.author}"
    
class Library:
    def __init__(self):
        self.inven = []

    def display(self):
        if not self.inven:
            return "empty"
        return self.inven

    def adds(self,book):
        for already in self.inven:
            if already.title == book.title and already.author == book.author:
                return f"Book already in the library"
        self.inven.append(book)
        return f"Book added succesfully"

    def remove(self,title,author):
        for book in self.inven:
            if book.title == title and book.author == author:
                self.inven.remove(book)
                return f"book have been removed"
        return f"Book Doesn't exist"
        
def menu():
    menu = (
       "=================================================\n"
        "Welcome to The Library\n"
        "\n1 Catalog\n"
        "2 Add Book\n"
        "3 Remove Book\n"
        "4 Exit\n"
        "\n"
        "=================================================" 
    )
    return menu

def pilihan():
    inputan = Library()
    while True:
        print(menu())
        choice = input("Choose 1-4: ")

        if choice == "1":
            ending = inputan.display()
            if isinstance(ending, list):
                for book in ending:
                    print(book)
            else:
                print(ending)

        elif choice == "2":
            title = input("Book Title: ")
            author = input("Author of The Book: ")
            book = Book(title,author)
            ending = inputan.adds(book)
            print(ending)

        elif choice == "3":
            title = input("Book title: ")
            author = input("Author of The Book: ")
            ending = inputan.remove(title,author)
            print(ending)
        
            
        elif choice == "4":
            print("let's meet another time")
            break

        else:
            print("Wrong Choice, Pick Again")

if __name__ == "__main__":
    pilihan()