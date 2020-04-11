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

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Open Address book(load json file)
    2.Print all person contacts
    ''')

def switchToFunction(case,filepath):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: open_addressbook(filepath),
        2 : lambda: printAllContacts(filepath),
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