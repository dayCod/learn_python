# CREATE PASSWORD GENERATOR APPS
# USING PYTHON

# === MODULES ===
import string
import random
# === TITLES ===
print("\n==== Welcome to Password Generator Apps With Python ====\n")
print("\nNote : please input a value higher than 7 and lower than 32\n")

# === GLOBAL VARIABLES ===
ask_for_start = input("Do you want to start using this password generator (Y/N) : ").upper()
continues = "Y"
stop = "N"

# === FUNCTIONS ===
def before_start():
    return ask_for_start

def start_password_generator(yes, no):
    result_before_start_func = before_start()
    if result_before_start_func == yes:
        pass_gen = password_generator()
        print(pass_gen)
    else:
        print("Byee !!")

def password_generator():
    user_input_length = int(input("Input a length of password : "))
    if user_input_length == 0:
        return f"you input a zero number, nothing to generate"
    elif user_input_length < 0:
        return f"you input a negative value, pls input a valid positive value"
    elif user_input_length >= 32:
        return f"please input a value lower than 32"
    elif user_input_length <= 7:
        return f"please input a value higher than 7"
    else:
        ran = "".join(random.choices(string.ascii_lowercase + string.digits + string.ascii_letters, k=user_input_length))
        return f"Here's a result : {ran}"

# START THE APPS
start_password_generator(continues, stop)


