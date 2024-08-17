import csv

class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}, {self.publication_year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        new_books = []
        for book in self.books:
            if book.title != title:
                new_books.append(book)
        if len(new_books) < len(self.books):
            self.books = new_books
            print(f"Book '{title}' removed from the library.")
        else:
            print(f"Book '{title}' not found in the library.")

    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def search_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def display_library(self):
        if not self.books:
            print('The library is empty.')
        else:
            for book in self.books:
                print(book)

    def save_to_file(self, filename='library.csv'):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Genre", "Year"])
            writer.writerows([[book.title, book.author, book.genre, book.publication_year] for book in self.books])
        print(f"Library saved to {filename}.")

    def load_from_file(self, filename='library.csv'):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                self.books = [Book(row[0], row[1], row[2], row[3]) for row in reader]
            print(f"Library loaded from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred while loading the file: {e}")

def main():
    library = Library()
    library.load_from_file()  # Load library data at startup

    while True:
        print("\nPersonal Library Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            publication_year = input("Enter publication year: ")
            book = Book(title, author, genre, publication_year)
            library.add_book(book)

        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == '3':
            title = input("Enter title: ")
            book = library.search_by_title(title)
            if book:
                print(book)
            else:
                print("Book not found.")

        elif choice == '4':
            library.display_library()

        elif choice == '5':
            library.save_to_file()
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
