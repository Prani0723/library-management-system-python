# Library Management System
# Created by Praneeth Kadiyala

books = {}

def add_book():
    name = input("Enter book name: ")
    if name in books:
        print("Book already exists!")
    else:
        books[name] = "Available"
        print("Book added successfully!")

def issue_book():
    name = input("Enter book name to issue: ")
    if name in books and books[name] == "Available":
        books[name] = "Issued"
        print("Book issued successfully!")
    else:
        print("Book not available!")

def return_book():
    name = input("Enter book name to return: ")
    if name in books and books[name] == "Issued":
        books[name] = "Available"
        print("Book returned successfully!")
    else:
        print("Invalid book!")

def view_books():
    if not books:
        print("No books in library")
    else:
        for book, status in books.items():
            print(f"{book} - {status}")

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        view_books()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")