print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
lowercase_string = combined_name.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

love = l + o + v + e
total = true + love

print(f"Your score is {total}%")

if total <=10 or total>=90 :
    print(f"your score is {total}%, You go together like coke and mentos.")
elif total >= 40 or total <=50 :
    print(f"your score is {total}%, You alright together.")
else :
    print(f"your score is {total}%.")    