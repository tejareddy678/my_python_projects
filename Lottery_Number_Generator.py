import random as rd
print("You should select your range!")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
n = int(input("How many times you want to draw: "))
List = [i for i in range(start,end + 1)]
print(f"Here are the draws you have achieved : {rd.sample(List,n)}")
