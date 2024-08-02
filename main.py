# contact_manager.py

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'Name: {self.name}, Phone: {self.phone}, Email: {self.email}'

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f'Contact {name} added.')

    def list_contacts(self):
        if not self.contacts:
            print('No contacts found.')
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print(f'No contacts found with the term: {search_term}')

def main():
    manager = ContactManager()

    while True:
        print('\nContact Manager')
        print('1. Add Contact')
        print('2. List Contacts')
        print('3. Search Contacts')
        print('4. Exit')

        choice = input('Enter choice (1/2/3/4): ')

        if choice == '1':
            name = input('Enter name: ')
            phone = input('Enter phone: ')
            email = input('Enter email: ')
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.list_contacts()
        elif choice == '3':
            search_term = input('Enter search term: ')
            manager.search_contact(search_term)
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
