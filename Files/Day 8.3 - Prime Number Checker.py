n = int(input("Check this number: "))

def prime_checker(number):
    if number == 1 :
        print("Its not a prime number, It's is a composite number")  
    elif number == 2 or number ==3 or number == 5 or number==7 :
        print("its a prime Number")
    elif number % 2 == 0:
        print("It's not a prime Number")
    elif number % 3 == 0 :
        print("It's not a prime Number")
    else:
        print("It's a prime Number")    

prime_checker(number=n)
