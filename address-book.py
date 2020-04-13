import json, os

class addressbook:

    def __init__(self, fname, lname, address, city, state, zipCode, phone):
        self._fname = fname
        self._lname = lname
        self._address = address
        self._city = city
        self._state = state
        self._zipCode = zipCode
        self._phone = phone 

    def __str__(self):
        return "First Name:{0}\nLast Name:{1}\nAddress:{2}\nCity:{3}\nState:{4}\nZip Code:{5}\nPhone No:{6}".format(self._fname,self._lname,self._address,self._city,self._state,self._zipCode,self._phone)
    
    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self,fname):
        self._fname = fname

    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self,lname):
        self._lname = lname

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        self._state = state
    
    @property
    def zipCode(self):
        return self._zipCode
    
    @zipCode.setter
    def zipCode(self, zipCode):
        self._zipCode = zipCode

    @property
    def phone(self, phone):
        return self._phone

    @phone.setter    
    def phone(self,phone):
        self._phone = phone

    @staticmethod
    def open_addressbook(filepath):
        """
        Function to open the address book file specified
        Returns the addressbook or None
        """
        path_exists = os.path.exists(filepath)
        addressbook = None
        if path_exists:
            try:                   # safest way to open or close file.
                with open(filepath, 'r') as infile:
                    addressbook = json.load(infile)
            finally:
                infile.close()
        return addressbook

    @classmethod
    def printAllContacts(cls,filepath):
        """
        Function to print list of all contacts details in the addressbook
        Returns 
        """
        address_books = cls.open_addressbook(filepath)
        if address_books:
            print("{:<10} {:<10} {:<30} {:<10} {:<15} {:<10} {:<10}".format('FNAME', 'LNAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE', 'PHONE NO'))
            for person in address_books['persons']:
                print("{:<10} {:<10} {:<30} {:<10} {:<15} {:<10} {:<10}".format(person['fname'],person['lname'],person['address'],person['city'],person['state'],person['zipCode'],person['phone']))
        else:
            print('No address book found!')

    @classmethod
    def add_contact(cls,filepath):
        """
        Function to add contact details to the addressbook
        It take user input and creates a contact that is added
        Returns 
        """
        new_contact = {}

        try:
            #new_contact['fname'] = input('Please enter the first name: ')
            new_fname = input('Please enter the first name: ')
            addressbook.fname = new_fname          # set first name 
            new_contact['fname'] = addressbook.fname    # get last name
            if not new_contact['fname']:
                raise ValueError('Error: Empty First Name')

            new_lname = input('Please enter last name: ')
            addressbook.lname = new_lname
            new_contact['lname'] = addressbook.lname
            if not new_contact['lname']:
                raise ValueError('Error: Empty Last Name')

            new_address = input('Please enter address: ')
            addressbook.address = new_address
            new_contact['address'] = addressbook.address
            if not new_contact['address']:
                raise ValueError('Error: Empty address')

            new_city = input('Please enter city name: ')
            addressbook.city = new_city
            new_contact['city'] = addressbook.city
            if not new_contact['city']:
                raise ValueError('Error: Empty City Name')

            new_state = input('Please enter state name: ')
            addressbook.state = new_state
            new_contact['state'] = addressbook.state
            if not new_contact['state']:
                raise ValueError('Error: Empty State Name')

            new_zipCode = input('Please enter zip code: ')
            addressbook.state = new_zipCode
            new_contact['zipCode'] = addressbook.state
            if not new_contact['zipCode']:
                raise ValueError('Error: Empty Zip Code')

            new_phone = input('Please enter phone number: ')
            addressbook.phone = new_phone
            new_contact['phone'] = addressbook.phone
            if not new_contact['phone']:
                raise ValueError('Error: Empty Phone Number')

        except ValueError as err:
            print(err)
            print('Contact not added.')
            exit()

        except KeyboardInterrupt:
            print('\nHiting the interrupt key.')
            exit()

            # Try to open the current addressbook
        address_books = cls.open_addressbook(filepath)

        if address_books is None:
            # If there was no addressbook create one
            print('Creating new address book')
            contacts = []
            address_books = {'persons': contacts}

        print(new_contact)
        try:
            with open(filepath, 'w') as outfile:
                # Write the output file with the new contact
                address_books['persons'].append(new_contact)
                json.dump(address_books, outfile, indent=4)
        finally:
            outfile.close()

    @classmethod
    def retrievePersonContact(cls,filepath):
        """
        Function to retirve specified contact details in the addressbook
        Returns a contact or None
        """
        print('Search data using: \n1.First Name\n2.Last Name\n3.City\n4.State')
        choice = int(input('Enter your choice: '))
        contact_details = []
        address_books = cls.open_addressbook(filepath)
        if not address_books:
            print('No address book found!')
        else:
            if choice == 1:
                fname = input('Enter First Name which contact you want to search: ')
                for person in address_books['persons']:
                    if person['fname'].casefold() == fname.casefold():      # casefold() convert string into lower case
                        contact_details.append(person)

            elif choice == 2:
                lname = input('Enter Last Name which contact you want to search: ')
                for person in address_books['persons']:
                    if person['lname'].casefold() == lname.casefold():
                        contact_details.append(person)

            elif choice == 3:
                city = input('Enter City Name which contact you want to search: ')
                for person in address_books['persons']:
                    if person['city'].casefold() == city.casefold():
                        contact_details.append(person)

            elif choice == 4:
                state = input('Enter State Name which contact you want to search: ')
                for person in address_books['persons']:
                    if person['state'].casefold() == state.casefold():
                        contact_details.append(person)
            
        if contact_details:
            print("{:<10} {:<10} {:<30} {:<10} {:<15} {:<10} {:<10}".format('FNAME', 'LNAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE', 'PHONE NO'))
            for person in contact_details:
                print("{:<10} {:<10} {:<30} {:<10} {:<15} {:<10} {:<10}".format(person['fname'],person['lname'],person['address'],person['city'],person['state'],person['zipCode'],person['phone']))
            return contact_details
        else:
            print("No contacts find")

    @classmethod
    def removePersonContact(cls,filepath):
        """
        Function to remove specified contact details from the addressbook
        Returns 
        """
        # Try to open the current addressbook and find the person contact
        address_books = cls.open_addressbook(filepath)
        persons = addressbook.retrievePersonContact(filepath)

        if persons:
            try:
                with open(filepath, 'w') as outfile:
                    # If contact was found delete it
                    for person in persons:
                        address_books['persons'].remove(person)
                    json.dump(address_books, outfile, indent= 4)
                    print('Contact removed.')
            finally:
                outfile.close()

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Open Address book(load json file)
    2.Print all person contacts
    3.Add new person contact in address book
    4.Retirve specified contact details in the addressbook
    5.Remove specified contact details from the addressbook
    ''')

def switchToFunction(case,filepath):
    '''
    Create switch function to move perticular program
    '''
    obj = addressbook
    switcher = {
        1 : lambda: obj.open_addressbook(filepath),
        2 : lambda: obj.printAllContacts(filepath),
        3 : lambda: obj.add_contact(filepath),
        4 : lambda: obj.retrievePersonContact(filepath),
        5 : lambda: obj.removePersonContact(filepath),
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    func()

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    FILE_PATH = "data/address_book_file.json"
    switchToFunction(choice,FILE_PATH)
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()