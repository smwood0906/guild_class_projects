# Take a list, say for example this one:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
final_lst = []
for i in a:
    if i < 5:
        final_lst.append(i)

print(final_lst)
# #
# # # Write this in one line of Python.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([i for i in a if i<5])
#
#
# # Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
final_lst = []
choice = int(input("Please enter any number. : "))
for i in a:
    if i < choice:
        final_lst.append(i)

print(final_lst)

#Above objective with list comprehension
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
choice = int(input("Please enter any number. : "))
print([i for i in a if i < choice])
