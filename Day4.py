#Create a Phonebook in Python using a dictionary. Ability to add, edit, search and remove entries. Day 4 of Bootcamp.

phonebook = {'sarah': {'name': 'Sarah', 'phone': '907-957-2865'}, 'adam': {'name': 'Adam', 'phone': '907-957-3470'}
}
def Search_entry():
    search = input('Who are you looking for? ')
    try:
        print('----'*10)
        print(phonebook[search.lower()]['name'])
        print(phonebook[search.lower()]['phone'])
        print('----'*10)
    except KeyError:
        query = input(search + ' not found. Would you like to add ' + search + ' to the phonebook? (y\\n): ')
        if query == 'y':
            Add_entry()

def Add_entry():
    add_entry = input('Enter the name of the person you\'d like to add to the phonebook: ')
    add_phone = input('Enter the phone number you\'d like to add for this contact: ')
    phonebook [add_entry.lower()] = {'name': add_entry.capitalize(), 'phone': add_phone}
    print( phonebook[add_entry.lower()]['name'] + ' has been added to the phonebook!')
    print('----'*10)
    print(phonebook[add_entry.lower()]['name'])
    print(phonebook[add_entry.lower()]['phone'])
    print('----'*10)

def Change_entry():
    edit_entry = input('Enter the name of person you\'d like to edit: ')
    try:
        print('----'*10)
        print(phonebook[edit_entry.lower()]['name'])
        print(phonebook[edit_entry.lower()]['phone'])
        print('----'*10)
        NC = False
        select = input('Would you like to change the name of this entry? (y\\n): ')
        if select.lower() == 'y':
            new_name = input('Enter the name you\'d like associated with this entry: ')
            NC = True

        select2 = input('Would you like to change the phone number for this entry? (y\\n):  ')
        if select2 == 'y':
            new_phone = input('Enter the phone number you\'d like associated with this entry: ')

            if NC == True and select2 == 'y':
                del(phonebook[edit_entry.lower()])
                phonebook[new_name.lower()] = {'name': new_name.capitalize(), 'phone': new_phone}
                print('----'*10)
                print(phonebook[new_name.lower()]['name'])
                print(phonebook[new_name.lower()]['phone'])
                print('----'*10)

            elif NC == True:
                new_phone = phonebook[edit_entry.lower()]['phone']
                del(phonebook[edit_entry.lower()])
                phonebook[new_name.lower()]= {'name': new_name.capitalize(), 'phone': new_phone}
                print('----'*10)
                print(phonebook[new_name.lower()]['name'])
                print(phonebook[new_name.lower()]['phone'])
                print('----'*10)

            elif select2 == 'y':
                phonebook[edit_entry.lower()]['phone'] = new_phone
                print('----'*10)
                print(phonebook[edit_entry.lower()]['name'])
                print(phonebook[edit_entry.lower()]['phone'])
                print('----'*10)

    except KeyError:
                print('Entry not found')

def Delete_entry():
    remove_entry = input('Who would you like to remove from the phonebook? ')
    answer = input('Are you sure you would like to remove ' + remove_entry + ' from the phonebook? (y\\n): ')
    if answer.lower() == "y":
        del(phonebook[remove_entry])
        print(remove_entry.capitalize() + ' has been removed from the phonebook.')


def phonebook_welcome():
    print('Welcome to the phonebook! ')
    while True:
        print('----'*10)
        print('To search for an entry, press 1: ')
        print('To add an entry, press 2: ')
        print('To change an entry, press 3: ')
        print('To delete an entry, press 4: ')
        print('To exit the phonebook, press 5: ')
        print('----'*10)
        try:
            choice = int(input('--> '))
            if choice == 1:
                Search_entry()
            elif choice == 2:
                Add_entry()
            elif choice == 3:
                Change_entry()
            elif choice == 4:
                Delete_entry()
            elif choice == 5:
                exit()
        except ValueError:
            print('That is not a valid entry. Please try again.')
            print('----'*10)

phonebook_welcome()
