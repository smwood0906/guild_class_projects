def game():
    print("Welcome to the A-Maze-ing Maze! I dare you to escape!")

    current_room = room0()

    while current_room != exit:
        current_room = current_room()

    current_room()


def process_user_movement(description, doors):

    print(description)
    options = list(doors.keys())

    print('You see doors to the '+ ', '.join(options[0:-1]) + ' and ' + options[-1] + '.')
    while True:
        choice = input('Which direction would you like to go? : ')
        if choice in options:
            return doors[choice]
        else:
            print('I didn\'t understand that, please try again.')
            print(' ')*40
            print('-->')


def room0():

    description = "This room is very small. You barely fit here. You're like \
    Alice in that crazy-tiny-room thing."
    doors = {'south': room6, 'east': room1, 'west': room2}

    return process_user_movement(description, doors)

def room1():
    description = 'room1'
    doors = {'south': room7, 'west': room0}
    return process_user_movement(description, doors)

def room2():
    description = 'room2'
    doors = {'south': room3, 'east': room0}
    return process_user_movement(description, doors)

def room3():
    description = "room3"
    doors = {'north': room2, 'west': room4, 'south': room5}
    return process_user_movement(description, doors)

def room4():
        description = "room4"
        doors = {'east': room3}
        return process_user_movement(description, doors)

def room5():
    description = 'room5'
    doors = {'north': room3}
    return process_user_movement(description, doors)

def room6():
    description = "room2"
    doors = {'north': room0, 'south': room8, 'east': room7}
    return process_user_movement(description, doors)

def room7():
    description = "room2"
    doors = {'north': room1, 'west': room6, 'east': room9, 'south': room10}
    return process_user_movement(description, doors)

def room8():
    description = "room2"
    doors = {'north': room6, 'south': final, 'east': room10}
    return process_user_movement(description, doors)

def room9():
    description = "room2"
    doors = {'west': room7}
    return process_user_movement(description, doors)

def room10():
    description = "room2"
    doors = {"north": room7, 'west': room8, 'east'}
    return process_user_movement(description, doors)

def final():
    description = "room2"
    doors = {'exit': exit}

game()
