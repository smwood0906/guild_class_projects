#Python program that creates a madlib from user input. Day 1 of Bootcamp.
one = input("Article of clothing: ")
two = input("Female name: ")
three = input("Another female name: ")
four = input("Male name: ")
five = input("Another male name: ")
six = input("Plural noun: ")

print("""{b2} and her ex-husband {d4}
were seen last night at the Twenty-Three Club holding
{f6}. Could it be reconcilliation? The international heartthrob,
{e5}, and the glamorous top
model, {c3}, are expecting their first
baby in November. {c3} is
denying stork rumors, but yesterday she was buying
a maternity {a1}.""".format(a1=one, b2=two, c3=three, d4=four, e5=five, f6=six))
