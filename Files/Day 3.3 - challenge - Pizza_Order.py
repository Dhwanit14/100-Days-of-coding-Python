print("Welcome to the Only Indian Pizza")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25\n")

print("Pepperoni for small Pizza: +2$")
print("Pepperoni for Medium or Large Pizza: +$3\n")

print("Extra cheese for any size pizza : +1$")



print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N : ").upper()
extra_cheese = input("Do you want extra cheese? Y or N : ").upper()
price = 0

if size == "S" :
    price = 15
    if add_pepperoni == "Y" :
        price += 2
    elif extra_cheese == "Y" :
            price += 1
elif size == "M" :
    price = 20 
    if add_pepperoni == "Y" :
        price += 3
    elif extra_cheese == "Y" :
            price += 1
elif size == "L" :
    price = 25
    if add_pepperoni == "Y" :
        price += 3
    elif extra_cheese == "Y" :
            price += 1
else :
    print("Choose a size from the above menu :")

print(f"Your final bill is {price} $")

