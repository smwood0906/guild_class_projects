n = 6
c = ['red', 'white', 'blue','blue', 'white', 'red']
possible = False
for i in range(n):
    if c[i] == "white":
        try:
            former = c[i - 1]
        except IndexError:
            former = None
        try:
            latter = c[i + 1]
        except IndexError:
            latter = None
        if former != latter:
            possible = True
        else:
            possible = False
            break
    try:
        if c[i] == c[i + 1]:
            possible = False
    except IndexError:
        pass

if possible == True:
    print('yes')
else:
    print('no')