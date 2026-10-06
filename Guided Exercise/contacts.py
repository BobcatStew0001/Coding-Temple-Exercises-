# contacts.py - A simple contact book using dictionaries

# Each contact is a dictionary; the whole book is a dictionary of contacts

contacts = {
    "alice" : {
        "fullname": "Alice Johnson",
        "phone": "555-0101",
        "email": "alice@example.com"
    },
    "bob": {
        "fullname": "Bob Smith",
        "phone": "555-0202",
        "email": "bob@example.com"
    }
}

def display_contacts():
    """Print all contacts in a formatted way"""
    print("\n" + "=" * 40)
    print("       Contact Book")
    print("=" * 40)

    if not contacts:
        print("No contacts yet.")
        return

    for key, info in contacts.items():
        print(f"\n {info['fullname']}")
        print(f"   Phone: {info['phone']}")
        print(f"   Email: {info['email']}")

    print(f"\n Total contacts: {len(contacts)}")
    print("=" * 40)

display_contacts()

#Look up a specific contact

search = input("\n Look up a contact (enter first name): ").lower()

contact = contacts.get(search) #.get() returns None if not found

if contact:
    print(f"\n Found: {contact['fullname']}")
    print(f"   Phone: {contact['phone']}")
    print(f"   Email: {contact['email']}")
else:
    print(f"\n No contact found for '{search}'.")

#Add a new contact
print("\n--- Add New Contact ---")
new_key = input("First name (for lookup): ").lower()
new_full = input("Full name: ")
new_phone = input("Phone: ")
new_email = input("Email: ")

contacts[new_key] = {
    "fullname": new_full,
    "phone": new_phone,
    "email": new_email
}

print(f"\n{new_full} added successfully!")
display_contacts()
