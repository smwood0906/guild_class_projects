def FizzBuzz():

    n = 100
    lst = list(range(0, n+1, 1))
    for number in lst:
        if number % 5 == 0 and number % 3 == 0:
            print('FizzBuzz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
            print('Fizz')
        else:
            print(number)

FizzBuzz()
