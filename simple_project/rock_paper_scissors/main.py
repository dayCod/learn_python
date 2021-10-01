# === Library ===
import random

# === Titles ===
print("\n===== Welcome To Rock Paper Scissor Game =====\n")

# === Global Variable ===
list_of_game = ["rock", "paper", "scissor"]
bracket_one = []
bracket_two = []
game_is_starting = True


# === Function ===
def generate_random_one():
    player_one_turns = player_one()
    return player_one_turns
    

def generate_random_two():
    player_two_turns = player_two()
    return player_two_turns


def player_one():
    # === Global ===
    global list_of_game

    range_of_list = range(0,3)
    generate_range_of_list = random.choice(range_of_list)
    index_list = list_of_game[generate_range_of_list]
    return index_list


def player_two():
    # === Global ===
    global list_of_game

    range_of_list = range(0,3)
    generate_range_of_list = random.choice(range_of_list)
    index_list_two = list_of_game[generate_range_of_list]
    return index_list_two


def roll_options():
    while game_is_starting:
        player_one_turn_ = generate_random_one()
        print("= Player's One Turn =")
        player_one_input = input("Next or Generate Random the option? (Y/N): ").upper()
        try:
            if player_one_input == "Y":
                bracket_one.append(player_one_turn_)
                last_index = bracket_one[-1]
                print("Player 1 : "+last_index+"\n")
            else:
                print("Player 1 Choice : "+bracket_one[-1]+"\n")
                break
        except IndexError:
            bracket_one.append(player_one_turn_)
            print("Player 1 Choice : "+bracket_one[0]+"\n")
            break

    while game_is_starting:
        player_two_turn_ = generate_random_two()
        print("= Player's Two Turn =")
        player_two_input = input("Next or Generate Random the option? (Y/N): ").upper()
        try:
            if player_two_input == "Y":
                bracket_two.append(player_two_turn_)
                last_index_two = bracket_two[-1]
                print("Player 2 : "+last_index_two+"\n")
            else:
                print("Player 2 Choice : "+bracket_two[-1]+"\n")
                break
        except IndexError:
            bracket_two.append(player_two_turn_)
            print("Player 2 Choice : "+bracket_two[0]+"\n")
            break


def check_winner(rock, paper, scissor):
    # Roll Option Function
    roll_options()
    # ==== Check the Winner ==== 
    
    # Player 1 vs Player 2 Check
    if bracket_one[-1] == rock and bracket_two[-1] == rock:
        print("Draw !!")
    elif bracket_one[-1] == rock and bracket_two[-1] == paper:
        print(paper+" Win !!")
    elif bracket_one[-1] == rock and bracket_two[-1] == scissor:
        print(scissor+" Win !!")
    elif bracket_one[-1] == paper and bracket_two[-1] == paper:
        print("Draw !!")
    elif bracket_one[-1] == paper and bracket_two[-1] == rock:
        print(paper+" Win !!")
    elif bracket_one[-1] == paper and bracket_two[-1] == scissor:
        print(scissor+" Win !!")
    elif bracket_one[-1] == scissor and bracket_two[-1] == scissor:
        print("Draw !!")
    elif bracket_one[-1] == scissor and bracket_two[-1] == rock:
        print(rock+" Win !!")
    elif bracket_one[-1] == scissor and bracket_two[-1] == paper:
        print(scissor+" Win !!")

    # Player 2 vs Player 1 Check
    elif bracket_two[-1] == rock and bracket_one[-1] == rock:
        print("Draw !!")
    elif bracket_two[-1] == rock and bracket_one[-1] == paper:
        print(paper+" Win !!")
    elif bracket_two[-1] == rock and bracket_one[-1] == scissor:
        print(scissor+" Win !!")
    elif bracket_two[-1] == paper and bracket_one[-1] == paper:
        print("Draw !!")
    elif bracket_two[-1] == paper and bracket_one[-1] == rock:
        print(paper+" Win !!")
    elif bracket_two[-1] == paper and bracket_one[-1] == scissor:
        print(scissor+" Win !!")
    elif bracket_two[-1] == scissor and bracket_one[-1] == scissor:
        print("Draw !!")
    elif bracket_two[-1] == scissor and bracket_one[-1] == rock:
        print(rock+" Win !!")
    elif bracket_two[-1] == scissor and bracket_one[-1] == paper:
        print(scissor+" Win !!")
    

# # === Start ===
check_winner(list_of_game[0], list_of_game[1], list_of_game[2])