import json        #for save and load operations
import os          #for file operations


data_file = "library.txt"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file)



def add_book(data):
    title = input("Enter Book Title:")
    author = input("Enter Book Author:")
    year = input("Enter Book Year:")
    genre = input("Enter Book Genre:")
    read = input("Have you read this book? (yes/no):").lower() == "yes"

    book ={
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }


    data.append(book)
    save_data(data)
    print(f'Book {title} added successfully!')


def remove_book(data):
        title = input("Enter the title of the book to remove:")
        for book in data:
            if book["title"].lower() == title.lower():
                data.remove(book)
                save_data(data)
                print(f'Book {title} removed successfully!')
                return
        print(f'Book {title} not found!')


def search_library (data):
    search_by = input("Search by (title/author/year/genre):").lower()
    search_term = input(f"Enter the ${search_by}:").lower()

    results = [book for book in data if search_term in book[search_by].lower()]

    if results: 
        for book in results:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
    else:
        print(f"No books found for {search_by}: {search_term}")

        
def display_all_books(data):
    if data:
        for book in data:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("No books in the library.")



def display_statistics(data):
    total_books = len(data)
    read_books = len([book for book in data if book["read"]])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Books Read in percentage: {percentage_read:.2f}%")



def main():
    data = load_data()

    while True:
        print("\nWelcome to the Library Manager")
        print("\nMenu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Library")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            add_book(data)
        elif choice == "2":
            remove_book(data)
        elif choice == "3":
            search_library(data)
        elif choice == "4":
            display_all_books(data)
        elif choice == "5":
            display_statistics(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
# This is a simple library manager program that allows users to add, remove, search, and display books in a library.