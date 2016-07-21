
import random

class Die():
    asci_die = {
    1:
    """
    +-------+
    |       |
    |   o   |
    |       |
    +-------+""",
    	2:
    """
    +-------+
    | o     |
    |       |
    |     o |
    +-------+""",
    	3:
    """
    +-------+
    | \   / |
    | ^   ^ |
    | ----- |
    +-------+""",
    	4:
    """
    +-------+
    | o   o |
    |       |
    | o   o |
    +-------+""",
    	5:
    """
    +-------+
    | o   o |
    |   o   |
    | o   o |
    +-------+""",
    	6:
    """
    +-------+
    | o   o |
    | o   o |
    | o   o |
    +-------+
    	""" }

    def __init__(self):
        self.value = 1
        self.art = self.asci_die[self.value]
        self.hold = False

    def roll(self):
        if self.hold == True:
            print(self.art)
        else:
            self.value = random.randint(1,6)
            self.art = self.asci_die[self.value]
            print(self.art)



class Players:
        def __init__(self, name):
            self.name = name
            self.die1 = Die()
            self.die2 = Die()
            self.phase = 1

        def round(self):
            print(self.name +', Die A rolled a: ')
            self.die1.roll()
            print(' and Die B rolled a: ')
            self.die2.roll()
            advance = self.check_win()

            if advance == False:
                choice = input('Would you like to hold the value of Die A or B? (enter A, B, or hit enter to continue without holding any die)')

                if choice.upper() == 'A':
                    if self.die1.value != 6:
                        self.die1.hold = True
                    else:
                        print('Sorry, you cannot hold a 6.')

                elif choice.upper() == 'B':
                    if self.die2.value != 6:
                        self.die2.hold = True
                    else:
                        print('Sorry, you cannot hold a 6.')


        def check_win(self):
            if self.die1.value == 3 and self.die2.value == 3:
                print('Your dice are so angry! Back to phase 1! ')
                self.phase = 1

            elif self.phase == 1 and self.die1.value + self.die2.value == 3:
                print(self.name + ' you\'re in Phase 2!')
                self.phase = 2
                self.die1.hold = False
                self.die2.hold = False
                return True

            elif self.phase == 2 and self.die1.value + self.die2.value == 7:
                print(self.name + ' you\'re in Phase 3!')
                self.phase = 3
                self.die1.hold = False
                self.die2.hold = False
                return True

            elif self.phase == 3 and self.die1.value + self.die2.value == 11:
                print(self.name + ' you win!')
                quit()
            return False

pl_lst = []
player1 = Players(input('What is the name of Player 1?: ').capitalize())
player2 = Players(input('What is the name of Player 2?: ').capitalize())
pl_lst.append(player1)
pl_lst.append(player2)

while True:
    for pl in pl_lst:
        pl.round()
