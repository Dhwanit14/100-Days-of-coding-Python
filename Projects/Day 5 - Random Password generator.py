import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters = ("".join(random.sample(letters, nr_letters))).lower()
symbols = ("".join(random.sample(symbols, nr_symbols))).lower()
numbers = ("".join(random.sample(numbers, nr_numbers))).lower()


# print(letters)
# print(numbers)
# print(symbols)

# combined the multiple list into a singe list
password = list(letters + symbols + numbers)

#shuffle the list
random.shuffle(password)

#converint the list back into the string to join it :
random_password = "".join(password)

#finally printing the list 
print(f"Your password is : {random_password}")