import random
print('The computer will choose a number between 1 and 100. Try to guess the number \n\
 in as few guesses as possible!')

def Guessing_Game():
    num = random.randint(1,101)
    win = False
    total = 0
    while win == False:
        guess = input('Please enter a number: ')
        if int(guess) == num:
            total += 1
            print('Congrats! You win! The number was ' + str(num) + '. Total guesses: ' + str(total))
            win == True
            exit()
        elif int(guess) > num:
            total += 1
            print('Good try, but your number is too high.')
            print('Number of guesses: ' + str(total))

        elif int(guess) < num:
            total += 1
            print('Guess again, your number is too low.')
            print('Number of guesses: ' + str(total))
        else:
            print('I didn\'t understand that, please try again.')
Guessing_Game()
