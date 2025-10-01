# Contact Book using Python (CLI)

# List to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("="*100)
    print("✅ Contact {} added successfully!".format(name))

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts available.\n")
    else:
        print("\n📒 Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
        print()

# Function to search contact by name
def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"🔍 Found: {contact['name']} | {contact['phone']} | {contact['email']}\n")
            found = True
            break

    if not found:
        print("❌ Contact not found.\n")

# Function to delete contact
def delete_contact():
    delete_name = input("Enter name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            print(f"🗑 Contact '{delete_name}' deleted successfully!\n")
            return
    print("❌ Contact not found.\n")

# Main program loop
def contact_book():
    while True:
        print("==== CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Try again.\n")

# Run program
contact_book()
