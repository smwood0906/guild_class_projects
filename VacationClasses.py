class Location():
    def __init__ (self, title, description, gates, stamp_text):
        self.title = title
        self.description = description
        self.gates = gates
        self.visited = False
        self.stamp_text = stamp_text


class Player():
    def __init__(self, name, location):
        self.name = name
        self.passport = Passport()
        self.location = location
        self.first = False

    def engine(self):
        print(self.location.title)
        if self.location.visited == False:
            self.stamping()
            self.display_stamps()
        elif self.location.visited == True:
            print('You have been here before! No passport stamp this time!')
        print(self.location.description)
        self.location.visited = True
        options = list(self.location.gates.keys())
        print('You could try '+ ', '.join(options[0:-1]) + ' or ' + options[-1] + '.')
        choice = input('Which adventure would you like to take? : ').capitalize()
        if choice in self.location.gates.keys():
            self.adventure(self.location.gates[choice])
        else:
            print('I didn\'t understand that, please try again.')
            print((' ')*40)
            print('-->')

    def adventure(self, title):
        self.location = title

    def first_class_check(self):
        if self.passport.total_stamps == 7:
            self.first = True

    def stamping(self):
        if self.location.visited == False:
            self.passport.stamp_list[self.location.title]= self.location.stamp_text
            self.passport.total_stamps += 1


    def display_stamps(self):
        print("Passport stamp message: " + self.passport.stamp_list[self.location.title])
        print("Number of stamps in your passport: " + str(self.passport.total_stamps))

class Passport():
    def __init__(self):
        self.total_stamps = 0
        self.stamp_list = {}

# create all locations
location1 = Location('Cabo', 'beaches', {}, "you are here")
location2 = Location('Amsterdam', 'drugs', {}, "what happened")

# list all gates
location1.gates = {'Bus': location2}
location2.gates = {'Train': location1}
player1 = Player('Sarah', location1)


while True:
    player1.engine()
    print()
