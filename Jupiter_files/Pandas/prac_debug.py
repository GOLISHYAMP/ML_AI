class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("List of Books:")
            for book in self.books:
                print(f"{book.title} by {book.author} ({book.year})")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display books")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the publication year of the book: ")
            new_book = Book(title, author, year)
            library.add_book(new_book)
            print("Book added successfully!")

        elif choice == "2":
            title_to_remove = input("Enter the title of the book to remove: ")
            library.remove_book(title_to_remove)
            print(f"{title_to_remove} removed successfully!")

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
