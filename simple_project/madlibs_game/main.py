# CREATE SIMPLE MADLIBS GAME FOR BEGINNER

# === TITLES ===
print("\n===== WELCOME TO MADLIBS GAMES =====\n")
print("\n===== Note : 0 => Indonesia || 1 => English =====\n")

# === GLOBAL VARIABLES ===
input_lang = int(input("Input your Language (0/1) : "))
eng = ["(1)", "(2)", "(3)", "(4)", "(5)", "(6)"]
ina = ["(1)", "(2)", "(3)", "(4)", "(5)", "(6)"]

# FUNCTIONS
def phrase():
    if input_lang == 1:
        print(f"\nIntroduce my name is {eng[0]}, i'm from {eng[1]}, i am {eng[2]} years old, my hobby is {eng[3]}, my favorite food is {eng[4]}, my favorite drink is {eng[5]}, Thank you")
    elif input_lang == 0:
        print(f"\nPerkenalkan nama saya {ina[0]}, saya dari {ina[1]}, umur saya {ina[2]} tahun, hobi saya {ina[3]}, makanan favorit saya adalah {ina[4]}, minuman favorite saya adalah {ina[5]}, Terima kasih")
    else:
        print("Wrong Num !!")

def start_madlibs():
    first_input = input("First Word : ")
    second_input = input("Second Word : ")
    third_input = input("Third Word : ")
    fourth_input = input("Fourth Word : ")
    fifth_input = input("Fifth Word : ")
    sixth_input = input("Sixth Word : ")

    if input_lang == 0:
        print(f"\nPerkenalkan nama saya {first_input}, saya dari {second_input}, umur saya {third_input} tahun, hobi saya {fourth_input}, makanan favorit saya adalah {fifth_input}, minuman favorite saya adalah {sixth_input}, Terima kasih")
    elif input_lang == 1:
        print(f"\nIntroduce my name is {first_input}, i'm from {second_input}, i am {third_input} years old, my hobby is {fourth_input}, my favorite food is {fifth_input}, my favorite drink is {sixth_input}, Thank you")
    else:
        return ""

    
    
phrase()
start_madlibs()
# START