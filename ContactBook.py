# ContactBook.py

import json
from contact import Contact  # ✅ Make sure this import exists

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = Contact(name, phone, email)
        print(f"✅ Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("❌ No contacts found!")
        else:
            for contact in self.contacts.values():
                print(contact)

    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print("❌ Contact not found!")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            print(f"✅ Contact '{name}' updated successfully!")
        else:
            print("❌ Contact not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"🗑 Contact '{name}' deleted successfully!")
        else:
            print("❌ Contact not found!")

    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump({name: vars(contact) for name, contact in self.contacts.items()}, file)
        print("💾 Contacts saved successfully!")

    def load_from_file(self, filename="contacts.json"):
        import os
        if not os.path.exists(filename):
            print("❌ No saved contacts found!")
            return

        if os.path.getsize(filename) == 0:
            print("📂 File is empty. Starting with an empty contact book.")
            return

        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.contacts = {name: Contact(**info) for name, info in data.items()}
                print("📂 Contacts loaded successfully!")
        except json.JSONDecodeError:
            print("❌ Failed to read contacts: Invalid JSON format.")
