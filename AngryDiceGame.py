
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
            pass
        else:
            self.value = random.randint(1,6)
            self.art = self.asci_die[self.value]
            print(self.art)



class Players:
        def __init__(self, name):
            self.name = name
            self.die1 = Die()
            self.die2 = Die()

        def round1(self):
            print(self.name +' Die A rolled a: ')
            self.die1.roll()
            print(' and Die B rolled a: ')
            self.die2.roll()
            if self.die1.value == 3 and self.die2.value == 3:
                print('Your dice are so angry! Back to Round 1! ')
            elif self.die1.value + self.die2.value == 3:
                return self.round2()
            else:
                choice = input('Would you like to hold the value of Die A or B? (enter A, B, or hit enter to continue without holding any die)')
                if choice.upper() == 'A':
                    self.die1.hold = True
                elif choice.upper() == 'B':
                    self.die2.hold = True



        def round2(self):
            print('round2')
# print('You rolled a {a} and a {b}!'.format(a = dice1, b = dice2))

player1 = Players(input('What is the name of Player 1?: '))
# player2 = Players(input('What is the name of Player 2?: '))
player1.round1()
