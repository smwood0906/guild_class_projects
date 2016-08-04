# Learning if else statements in Python. Day 2 of Bootcamp.

if "Some text" == "some text":
    print("Yes")
else:
    print("No")

if (-4 < -6) and (2 < 4):
    print("Yes")
else:
    print ("No")

if "part" in "party!!!1":
    print("Yes")
else:
    print("No")

age = input("How old are you? ")
if 102 > int(age) > 0:
    print("You are " + age + "!")
else:
    print("Liar!")

answer = input("What is the capital of Alaska? ")
if answer.lower() == "juneau":
     print("Excellent, you really know your capitals!")
elif answer.lower() == "juno":
    print("Close, your spelling is a little off.")
else:
    print("Nope, go buy a map!")
