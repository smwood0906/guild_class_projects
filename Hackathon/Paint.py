n = 5
c = ['blue', 'white', 'white', 'red', 'blue']
possible = False
for i in range(n):
    if c[i] == "white":
        if c[i - 1] == "blue":
            c[i] = c[i].replace("white", "red")
        elif c[i - 1] == "red":
            c[i] = c[i].replace("white", "blue")
for i in range(n):
    try:
        if c[i] != c[i + 1]:
            possible = True
        else:
            possible = False
            break
    except IndexError:
        pass
if possible == True:
    print('yes')
else:
    print('no')
