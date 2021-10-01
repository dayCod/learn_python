# SIMPLE BASIC CALCULATOR WITH PYTHON
# + - / * - (addition, multiplication, division, subtraction)

# === TITLES ===
print("\n===== Basic Calculator =====\n")

# === GLOBAL VARIABLES ===
plus = "+"
minus = "-"
divide = "/"
times = "*"
first_value = int(input("Input the first value : "))
second_value = int(input("Input the second value : "))
operation = input("Input an operation (+, -, /, *) : ")

# === FUNCTIONS ===
def execute():
    calculated = calculating(first_value, second_value)
    return f"Here's the result : {calculated}"

def calculating(num1, num2):
    if operation == plus:
        return num1 + num2
    elif operation == minus:
        return num1 - num2
    elif operation == divide:
        return num1 / num2
    elif operation == times:
        return num1 * num2
    else:
        return "Wrong operation !!"
           
# START 
start_the_calculator = execute()
print(start_the_calculator)
