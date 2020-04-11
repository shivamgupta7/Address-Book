import json, os

class addressbook:

    def __init__(self, fname, lname, address, city, state, zipCode, phone):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.phone = phone 

    def __str__(self):
        return "First Name:{0}\nLast Name:{1}\nAddress:{2}\nCity:{3}\nstate:{4}\nZip Code:{5}\nPhone No:{6}".format(self.fname,self.lname,self.address,self.city,self.state,self.zipCode,self.phone)

def open_addressbook(filepath):
    """
    Function to open the address book file specified
    Returns the addressbook or None
    """
    path_exists = os.path.exists(filepath)
    addressbook = None

    if path_exists:
        with open(filepath, 'r') as infile:
            addressbook = json.load(infile)
    
    return addressbook

def printAllContacts(filepath):
    """
    Function to print list of all contacts details in the addressbook
    Returns 
    """
    addressbook = open_addressbook(filepath)
    if addressbook:
        for person in addressbook['person']:
            print('First Name: ' + person['fname'], 'Last Name : ' + person['lname'], 'Address: ' + person['address'], 'City: ' + person['city'], 'State: ' + person['state'], 'Zip: ' + person['zipCode'], 'Telephone: ' + person['phone'], sep='\t', end='\n' )
    else:
        print('No address book found!')

def add_contact(filepath):
    """
    Function to add contact details to the addressbook
    It take user input and creates a contact that is added
    Returns 
    """
    new_contact = {}
    new_fname = input('Please enter the first name: ')

    # Have we got a name to add?
    if new_fname:
        new_contact['fname'] = new_fname
        new_contact['lname'] = input('Please enter last name: ')
        new_contact['address'] = input('Please enter their address: ')
        new_contact['city'] = input('Please enter city name: ')
        new_contact['state'] = input('Please enter state name: ')
        new_contact['zip'] = str(input('Please enter zip code: '))
        new_contact['phone'] = str(input('Please enter their phone number: '))

        # Try to open the current addressbook
        addressbook = open_addressbook(filepath)

        if addressbook is None:
            # If there was no addressbook create one
            print('Creating new address book')
            contacts = []
            addressbook = {'person': contacts}

        print(new_contact)
        with open(filepath, 'w') as outfile:
            # Write the output file with the new contact
            addressbook['person'].append(new_contact)
            json.dump(addressbook, outfile, indent=4)

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Open Address book(load json file)
    2.Print all person contacts
    3.Add new person contact in address book
    ''')

def switchToFunction(case,filepath):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: open_addressbook(filepath),
        2 : lambda: printAllContacts(filepath),
        3 : lambda: add_contact(filepath)
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    print(func())

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