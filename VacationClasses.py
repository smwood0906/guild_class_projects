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
        if self.location.title == 'exit':
            exit()
        else:
            self.random_reset()
            print('-'*40)
            print(self.location.title)
            if self.location.visited == False:
                self.stamping()
                self.display_stamps()
                self.first_class_check()
            elif self.location.visited == True:
                print('You have been here before! No passport stamp this time!')
            print('-' *40)
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
        if self.passport.total_stamps == 8:
            self.first = True
            print('Congratulations! You\'ve achieved First Class status FOR LIFE!!!!')

    def stamping(self):
        if self.location.visited == False:
            self.passport.stamp_list[self.location.title]= self.location.stamp_text
            self.passport.total_stamps += 1

    def display_stamps(self):
        print("Passport stamp message: " + self.passport.stamp_list[self.location.title])
        print("Number of stamps in your passport: " + str(self.passport.total_stamps))

    def random_reset(self):
        n = random.randint(0,15)
        if n == 7 or n == 13:
            print('''Oh no! Due to some misunderstanding with the local authorities you\'ve\n\
            been sent home! Keep going to search for the final destination, or work toward your\n\
            First Class status. ''')
            self.location = location1


class Passport():
    def __init__(self):
        self.total_stamps = 0
        self.stamp_list = {}

# create all locations
location1 = Location('Portland', '''Looks like you\'re at the Portland airport. While the food here is delicious,\n\
 and reasonably priced, this carpet is making you dizzy.\
 \n\
 There are three flights leaving soon that you\'ve got time to catch.''', {}, 'Is there gluten in that?')

location2 = Location('Cabo', '''Viva Mexico!  You spend a few days relaxing on Medano beach, sipping 2 for 1 margaritas\n\
and getting a tan. You head up to Todos Santos for a day and visit the Hotel California, then come back for\n\
an evening water taxi to Lover's Beach.\n\

You\'re starting to feel a little dehydrated and worn out from all the heat. A couple you met at Cabo Wabo offered you\n\
their hometown apartment as a place to stay while they finish their time in Mexico.\n\

You could call the airline and change your flight, or take your chances on the next flight that leaves\n\
 no matter where it\'s headed.''', {}, 'Salt that rim!')

location3 = Location('Amsterdam', '''Amsterdam!! Somehow it has been two days since you arrived, but you can\'t remember the first one. \n\
\n\
You find ticket stubs to the Anne Frank House and the Van Gogh Museum in your wallet, so it seems like a good trip so far!\n\
It also appears that you have maxed out your credit card, which limits your options to the $78 in cash you have in \n\
your wallet. Well, that and your unmatched charm.\n\
\n\
There is a bus headed South that you can afford, you can take that stranger up on their offer for a place to crash for the night,\n\
or you can call your Mom and beg for a flight home.''', {}, 'Just act normal and you\'ll be crazy enough.')

location4 = Location('Paris', '''Paris! You\'ve managed to squeeze in a trip the Louvre,\n\
the Eiffel Tower, and Notre Dame. But, you\'ve also had your fill of wine and cheese and are ready to head to your\n\
next destination.\n\
\
You get a killer flight deal alert on your phone, but can\'t see where to.\n\
You\'ve also been dying to take the Chunnel (underwater train) to London.\n\
You\'re also tempted to join some new friends from the hostel on a ski trip to Switzerland.''', {}, 'Bonjour!')

location5 = Location('London', '''London would probably be more fun if your wallet and passport hadn\'t been stolen on the tube! Lucky for you,\n\
you charmed the pants off the security guard at Big Ben. Who could have known it was the Queen\'s third cousin? \n\
Maybe if you\'re lucky she can help you get back some identification and funding and send you on to your next desination!\n\
Do you want to meet the Queen, or take your chances with the embassy?''', {}, 'What a brilliant holiday!')

location6 = Location('Switzerland', '''Switzerland! What an incredible three days of skiing in the Swiss Alps! It snowed every \n\
day making the powder something you\'d only ever dreamed about! Unfortunately, all that snow has closed down most transportation \n\
options and it looks like you\'re either going to have to go back the way you came or hitch a ride with that ski racing team \n\
on their bus.''', {}, 'Gruetzi!')

location7 = Location('Vegas', '''Vegas baby! You\'ve now been awake for three days straight! \n\
You got married by Elvis, then had it anulled a few hours later. You\'ve been a special guest on\n\
three separate bachelorette party buses, and you\'re seriously considering a career change to the Cirque du Soleil.\n\
\n\
You\'re about out of money, but can\'t resist one more roll at the craps table... JACKPOT!\n\
Should you take that expensively dressed gentleman up on his offer\n\
to discuss a business proposition in his suite? Shoot, you could also just buy a private jet with your winnings\n\
and fly anywhere you want! ''', {}, 'What happens in Vegas, stays in Vegas!')

location8 = Location('Iceland', '''You\'ve always wondered what Iceland would be like! After viewing some fantastic northern lights in Reykjavik, \n\
and a relaxing spa weekend at the Blue Lagoon hot pools, it\'s time for another adventure.\n\
\n\
You are tempted by that couple\'s offer to join them on their kayak trip in Greenland to look for narwhals, \n\
it is your favorite animal after all.\n\
You could also leave all this cold weather behind and head for a nice beach somewhere.\n\
There\'s also this guilt that\'s been building, maybe you should learn something historical on your next trip?.\n\
Then again, some rowdy American nightlife might be a nice way to mix things up.''', {}, 'On with the butter!')

location9 = Location('Zanzibar', '''Zanzibar! How were you supposed to know talking with that guy would land you here? \n\
Accidentally ending up on an island with crystal white beaches isn\'t a bad surprise though.\n\
\n\
You hop on the ferry to Tanzania, take a quick jog up Kilimanjaro, then finish off with a short \n\
safari to the Ngorongoro Crater and the Serengeti. Not a bad trip, but these malaria pills are \n\
giving you crazy dreams and you\'re ready to head out.\n\
\n\
You can take your new friend\'s offer for a flight back to where you started.\n\
Or, you can let the agent at the travel counter pick your next destination for you.''', {}, 'Hakuna Matata')

location10= Location('Greenland', '''Greenland! After a cold, exhausting, and exciting kayak trip you finally see your favorite animal, the narwhal, \n\
in real life! Next up is a visit to the viking ruins and the Hvalsey Fjord Church. Then one more stop at the breathtaking\n\
Illulissat ice-fjord.\n\
\n\
All these chilly endeavors are making you long for those sweet Icelandic hot pools though.\n\
One more dip in the springs, or take a chance with your travel app again?''', {}, 'The unicorns of the sea!')

location11 = Location('Egypt', '''Egypt! This has to be the Final Destination on your vacation adventure\n\
 because you are running dangerously low on funds!\n\
 \n\
 But first, you play tourist at the Great Pyramids, the Sphinx, and the Valley of the Kings.\n\
\n\
 You can head to the travel agency to finish your adventure, or, if you are still trying for for First Class status,\n\
  you could try to keep going on the cheap and go with this slightly\n\
  shady looking fellow who is offering to take you to King Tut's tomb for free.''', {}, 'This stamp is a curse!')

location12 = Location('exit', '', {}, '')

# list all gates
location1.gates = {'Vegas': location7,'Cabo': location2, 'Amsterdam': location3}
location2.gates = {'Apartment': location8, 'Chance': location4}
location3.gates = {'Bus': location4, 'Mom': location1, 'Stranger': location9}
location4.gates = {'Flight': location7, 'Chunnel': location5, 'Skiing': location6}
location5.gates = {'Queen': location4, 'Embassy': location7}
location6.gates = {'Backtrack': location4, 'Bus': location3}
location7.gates = {'Business': location9, 'Jet': location8}
location8.gates = {'Beach': location2, 'Usa': location7, 'Kayak': location10, 'History': location11}
location9.gates = {'Backtrack': location7, 'Agent': location8}
location10.gates = {'Springs': location8, 'Chance': location11}
location11.gates = {'Tomb': location7, 'Agency': location12}

player1 = Player('Sarah', location1)
import random
print('''Welcome to your Vacation Adventure!\n\
Make choices to travel to different destinations and gather passport stamps\n\
along the way. You must find the Final Destination to finish the game.\n\
Try to avoid getting sent home to Portland to restart your adventure.\n\
Get at least 8 different passport stamps to acheive First Class status for life!''')
while True:
    player1.engine()
