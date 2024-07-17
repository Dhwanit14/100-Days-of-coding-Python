print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

step1 = input("""You're at a cross road. Where do you want to go? Type "left" or "right" """).upper()


if step1 == "LEFT": 
    step2 = input("""You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "Swim" to swim across the island - """).lower()
    if step2 == "wait" :
        step3 = input("you have arrived the island unharmed. There isa house with 3 doors. One red, One yellow and one blue. Which colour do you want to choose ? - ").lower()
        if step3 == "red" :
            print("It's a room full of Fire. GAME OVER!!")
        elif step3 == "yellow" :    
            print("You have enter a room of beast. GAME OVER!!")
        elif step3 == "blue" :
            print("You have found the treasure. You win ¯\_( ͡❛ ͜ʖ ͡❛)_/¯")
    else:
        print("you get attacked by an angry trout and lose")
else :
    print("OOPS! , you fell into a hole. GAME OVER!!")         