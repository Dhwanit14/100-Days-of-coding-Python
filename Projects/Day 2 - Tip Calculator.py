print("welcome to the tip Calculator")

total_bill = float(input("What was the total amount of bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 15, 20 :"))

split = int(input("how many people to split this bill : "))

adding_tip = (total_bill) * (tip /100) 

total_bill = total_bill + adding_tip

split = round(total_bill / split , 2) 

print(f"Each person should have {split}$ to split !")