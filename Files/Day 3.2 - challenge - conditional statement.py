# Program to check whether a number is a odd or an even number :

# a = int(input("Write your number : "))

# if a % 2 == 0 :
#     print("Your number is even")
# else :
#     print("Your number is odd")


# elif condition

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))

  if age < 12 :
    bill = 5
    print("child tickets are $5.")
  elif age <= 18: # between 12 & 18
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age<=55:
    print("Everything is oing to be ok, Enjoy your ride !!")
  else: # over 18
    bill = 12
    print("Youth tickets are $12.")

  wants_photo = input("Do you want a photo ticket ? Y or N. ").upper()
  if wants_photo == "Y" :
    bill += 3 #Adding 3$ to the bills

  print(f"Your final bill is : {bill}")


else:
  print("Sorry, you have to grow taller before you can ride.")


# challenge 1 - conditional statement

# 🚨 Don't change the code below 👇
# weight = float(input("enter your weight in kg: "))
# height = float(input("enter your height in m: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# weight = float(input("enter your weight in kg: "))
# height = float(input("enter your height in m: "))
# BMI = (weight) / (height ** 2)

# if BMI < 18.5 :
#   print("You are underweight")
# elif BMI < 25 :
#         print("You are normal weight")
# elif BMI < 30 :
#         print("You are overweight")
# elif BMI < 35 :
#         print("You are obese")
# elif BMI > 35:
#         print("You are critically obese")
# else :
#   print(int(BMI))  



# challenge 2 - leap year or not

# print("Welcome to the calcualtor that checks whether the year is a leap year or not !!")

# year = int(input("Enter the year : "))

# if year % 4 == 0:
#     if year % 100 == 0 :
#         if year / 400 ==0:
#             print("The year is a leap year !!")
#         else :
#             print("The year is not a leap year !!")
#     else :
#         print("The year is a leap year !!")
# else :
#     print("The year is not a leap year !!")

# if (year%4 == 0 and year%100 !=0 ) or (year%400 ==0):
#     print(f"The year {year} is a leap year !!")
# else :
#     print(f"The year {year} is not a leap year !!")


