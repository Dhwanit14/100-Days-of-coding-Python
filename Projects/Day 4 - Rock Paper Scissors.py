import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

sign3 = [rock , paper , scissors]

#computer takes any index from the above list and be saved as int:
computer_selection = random.randint(0,2)

# user input the number and be saved as int
user_selection = int(input("What do you want to choose? Type 0 for Rock, 1 for paper or 2 for Scissors: "))


if user_selection>=3 or user_selection<0 :
    print("You have entered a invalid number, Try again !!")
else :    
    print(f"You have selected \n{sign3[user_selection]}")
    print(f"Computer have selected \n{sign3[computer_selection]}")


if user_selection>=3 and user_selection<0 :
    print("You have entered a invalid number, Try again !!")
elif user_selection == 2 and computer_selection ==1:
    print("you win!!")
elif user_selection ==1 and computer_selection ==1:
    print("you win!!")
elif user_selection ==0 and computer_selection ==2:
    print("you win!!")
elif user_selection == computer_selection :
    print("It's a DRAW")

else :    
    print("You Loose !! ")
