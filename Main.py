# Main.py

from ContactBook import ContactBook

def main():
    contact_book = ContactBook()
    contact_book.load_from_file()

    while True:
        print("\n📖 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None)

        elif choice == "5":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            contact_book.save_to_file()
            print("👋 Exiting Contact Book. Have a great day!")
            break

        else:
            print("❌ Invalid option! Please choose a valid option.")

if __name__ == "__main__":
    main()
