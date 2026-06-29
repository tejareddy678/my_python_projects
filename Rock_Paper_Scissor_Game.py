import random as rd
user_score = 0
computer_score = 0
def result(user_choice : str,computer_choice : str) -> str :
    if(user_choice == "Rock" and computer_choice == "Scissor"):
        return "You Won"
    elif(user_choice == 'Rock' and computer_choice == "Paper"):
        return "You Lost"
    elif(user_choice == "Scissor" and computer_choice == "Rock"):
        return "You Lost"
    elif(user_choice == "Scissor" and computer_choice == "Paper"):
        return "You Won"
    elif(user_choice == "Paper" and computer_choice == "Scissor"):
        return "You Lost"
    elif(user_choice == "Paper" and computer_choice == "Rock"):
        return "You Won"
    elif(user_choice == computer_choice):
        return "Draw"
choices = ["Rock","Paper","Scissor"]
isplay = input("Dear user do you want to play the game? : ").capitalize()
if(isplay == "No"):
    print("Thank You🤦‍♂️")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
while(isplay == "Yes"):
    user_choice = input("Dear User Please select your choice (Rock | Paper | Scissor): ").capitalize()
    computer_choice = rd.choice(choices)
    while(user_choice not in choices):
        print("Dear User please select only either [Rock | Paper | Scissor]")
        user_choice = input("Dear User Please select your choice (Rock | Paper | Scissor): ").capitalize()
    print(f"You have chosen {user_choice}")
    print(f"Computer have chosen {computer_choice}")
    res = result(user_choice,computer_choice)
    print(res)
    if(res == "You Won"):
        user_score = user_score + 1
    elif(res == "Draw"):
        user_score = user_score
        computer_score = computer_score
    else:
        computer_score = computer_score + 1
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    isplay = input("Dear user do you want to play the game? : ").capitalize()
    if (isplay == "No"):
        print("Thank You🤦‍♂️")
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
