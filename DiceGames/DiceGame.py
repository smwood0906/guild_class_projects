
def DiceGame():
    print('Welcome to the Dice Game! Take turns rolling the dice.\
The first player to reach 20 wins. If you exceed 20 on your roll, \
you must roll again until you get a number that gets you exactly to 20.\
If you roll double 3\'s or double 6\'s your score resets to 0.\
Grab a partner and get ready to play!')
import random

class Players:
        def __init__(self, name):
            self.name = name
            self.score = 0

        def roll(self):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            print('You rolled a {a} and a {b}!'.format(a = dice1, b = dice2))
            if dice1==3 and dice2==3 or dice1==6 and dice2==6:
                self.score == 0
                print ('You rolled double {a}\'s! Your score is now {s}.'.format(a = dice1, s = self.score))
            else:
                addscore = dice1 + dice2
                self.score += addscore
                print('{n} your score is now {s}!'.format(n=self.name, s=self.score))

player1 = Players(input('What is the name of Player 1?: '))
player2 = Players(input('What is the name of Player 2?: '))

while player1.score <= 20 and player2.score <= 20:
    input('{p1} it\'s your turn! Press Enter to roll: '.format(p1 = player1.name))
    player1.roll()
    if player1.score >= 20:
        print('Congratulations {p1}, you win!'.format(p1 = player1.name))
        exit()
    input('{p2} it\'s your turn! Press Enter to roll: '.format(p2 = player2.name))
    player2.roll()
    if player2.score >= 20:
        print('Congratulations {p2}, you win!'.format(p2 = player2.name))
        exit()
