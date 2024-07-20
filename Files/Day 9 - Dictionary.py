programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print(programming_dictionary["Bug"])

#adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something again and again." 
# print(programming_dictionary)

#Create empty dictionary
empty_dictionary = {}

#loop through a dictionary
for i in programming_dictionary:
    print(i)
    print(programming_dictionary[i])