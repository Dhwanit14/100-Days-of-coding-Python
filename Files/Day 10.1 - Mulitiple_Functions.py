#fucntion with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "" :
        return "you didnot provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("Whats your first name: "),input("Whats your last name: ")))

# format_name("dhWaNit","Dhwanit")