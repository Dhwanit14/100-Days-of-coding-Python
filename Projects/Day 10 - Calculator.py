from arts import calculator_logo

#calculator
print(calculator_logo)
#Add
def add (n1,n2):
    return n1+n2

#Subtract
def subtract (n1,n2):
    return n1-n2

#Multiply
def multiply (n1,n2):
    return n1*n2

#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue : 
            operation_symbol = input("Pick an operation: ") 
            num2 = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol] 
            answer = calculation_function(num1,num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            user_choice = input(f"Type 'y' to continue calulating with {answer}, or type 'n' to exit>:  ")

            if user_choice == "y" :         
                num1 = answer
            else :
                should_continue = False
                print("Thanks for using my calculator service!!")
                calculator()

calculator()