# # simple Function
# def greet():
#     print("Hello Angela")
#     print("How do you do ?")
#     print("Isn't a nice weather today?")

# greet()

#function the takes input = parameters
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")

# greet_with_name("Zeel")

#functions that the more than 1 input
# def greet_with(name,location):
#     print(f"Hello {name}, How are you ?")
#     print(f"How is the weather today in {location} ?")

# greet_with("Dhwanit","Dholka")

#function that can take keyword arguments
def greet_with(name,location):
    print(f"Hello {name}, How are you ?")
    print(f"How is the weather today in {location} ?")

greet_with(location="Dholka",name="Dhwanit")