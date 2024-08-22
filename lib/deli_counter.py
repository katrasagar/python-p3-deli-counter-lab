# Function to display the current line
def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        for i, person in enumerate(katz_deli):
            line_status += f" {i+1}. {person}"
        print(line_status)

# Function to add a customer to the end of the line
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

# Function to serve the next customer in line
def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_customer = katz_deli.pop(0)
        print(f"Currently serving {current_customer}.")

