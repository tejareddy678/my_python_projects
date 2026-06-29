import random as rd
symbols = ["🤑","🤡","🥃","🔥"]
balance = 100
def spin(balance : int,bet : int):
    Set = set()
    res = []

    balance = balance - bet
    for i in range(3):
        draw = rd.choice(symbols)
        res.append(draw)
        Set.add(draw)
    print(" | ".join(res))
    if(len(Set) == 1):
        print("Jackpot!")
        return balance + bet * 100
    elif(len(Set) == 2):
        print("Duos!")
        return balance + bet * 10
    else:
        print("You Lost!")
        return balance
    Set.clear()
    res.clear()
isPlay = input("Dear user do you want to spin (Yes / No): ").capitalize()
print("")
while(isPlay not in ["Yes","No"]):
    print("You can select (Yes / No) no more other options")
    isPlay = input("Please select your choice(Yes / No) : ").capitalize()
    print("")
while(isPlay == "Yes"):
    if(balance == 0 or balance < 0):
        print("You are out of money!")
        break
    bet = int(input("Enter Your bet : "))
    print("")
    while(bet < 0 or bet == 0 or bet > balance):
        print("Bet should not be zero or negative or more than current balance please choose again!")
        print(f"Your current balance is {balance}")
        bet = int(input("Enter your bet again: "))
        print("")
    balance = spin(balance,bet)
    print(f"Your current balance is {balance}$\n")
    isPlay = input("Dear user do you want to spin again (Yes / No): ").capitalize()
    print("")
    while(isPlay not in ["Yes", "No"]):
        print("You can select (Yes / No) no more other options")
        isPlay = input("Please select your choice(Yes / No) : ").capitalize()
        print("")
print("Thank you!")
print(f"Your current balance is {balance}")







