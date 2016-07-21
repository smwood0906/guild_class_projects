# Given 3 int values, a b c, return their sum. However, if
# one of the values is 13 then it does not count towards
# the sum and values to its right do not count. So for
# example, if b is 13, then both b and c do not count.

def trickySum(a,b,c):
    intList = [a,b,c]
    total = 0
    for i in range(0,len(intList)):
        if intList[i] == 13:
            print(total)
        elif intList[i] != 13:
            total = total + intList[i]
            print(total)




trickySum(2,13,2)

