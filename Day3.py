#Learning how to create Functions in Python. Day 3 of Bootcamp.


def question(answer):
    if answer == '42':
        print('You are correct!')
    else:
        print('Nope, try again.')
ans = input('WHat is the meaning of everything? ')
question(ans)


def addNumber(x,y):
    print(x+y)

addNumber(65, 78)

def subtractNumber(x,y):
    print(x-y)

subtractNumber( 56, 89)

def getBiggerNumber(x,y):
    print( max(x,y))

getBiggerNumber(57,26)


def isEquilateral(x,y,z):
    if x == y and y==z and z==x:
        return True
    else:
        return False
print(isEquilateral(6,5,5))

def addFirstandLastx(lst):
    return sum((int(lst[0]), int(lst[-1])))
print(addFirstandLastx([5,6,7]))

def isEven(number):
    if number % 2 == 0:
        return True
print(isEven(6))

def twentyfour(hour,am_or_pm):
    if (am_or_pm == 'am'):
        return hour
    elif (am_or_pm == 'pm'):
        return (hour + 12)
    else:
        return ("Please specify 'am' or 'pm': ")
print(twentyfour(3,'pm'))

def countA(word):
    return word.count('a')
print(countA('abagaafasgaha'))

def countLetter(word, letter):
    word = str(word)
    letter = str(letter)
    return word.count(letter)
print(countLetter("apple", "p"))

def changeCase(word):
    word = str(word)
    new_word = ""
    for letter in word:
        if letter.islower():
            new_word += letter.upper()
        elif letter.isupper():
            new_word += letter.lower()
        else:
            new_word += letter
    return new_word
print(changeCase("HavaNa1"))

def TwentFourConvert(t):
    import datetime
    import time
    new_time = int(t)
    print(new_time.time.hour())
print( TwentFourConvert(3))
