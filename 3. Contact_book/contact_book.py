contacts = []
names = set()
recently_viewed = []


def add_contact():
    name = input("Enter the name: ").strip()
    name_key = name.lower()

    if name_key in names:
        print("already exists")
        return

    phone_number = input("Enter the phone number: ").strip()
    email = input("Enter the email: ").strip()

    contacts.append(
        {"name": name, "phone": phone_number, "email": email}
    )
    names.add(name_key)


def list_contacts():
    if not contacts:
        print("Contact book is empty.")
        return

    for contact in contacts:
        print(
            f"Name: {contact['name']}, "
            f"Phone: {contact['phone']}, "
            f"Email: {contact['email']}"
        )


def search_contact():
    search_name = input("Enter the name to search: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == search_name:
            print(
                f"Name: {contact['name']}, "
                f"Phone: {contact['phone']}, "
                f"Email: {contact['email']}"
            )
            recently_viewed.append(contact["name"])
            del recently_viewed[:-5]
            return

    print("not found")


def delete_contact():
    name_to_delete = input("Enter the name to delete: ").strip()
    name_key = name_to_delete.lower()

    if name_key not in names:
        print("not found")
        return

    contacts[:] = [
        contact for contact in contacts if contact["name"].lower() != name_key
    ]
    names.remove(name_key)


def show_recently_viewed():
    if not recently_viewed:
        return

    for name in recently_viewed:
        print(name)


def main():
    while True:
        print(
            "1. Add\n"
            "2. List\n"
            "3. Search\n"
            "4. Delete\n"
            "5. Show recently viewed\n"
            "6. Quit"
        )
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            show_recently_viewed()
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
