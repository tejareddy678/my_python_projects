import random as rd
score = 0
questions = {
    "What is the capital of India?\n1.Washington\n2.New Delhi\n3.Canberra\n4.Moscow" : 2,
    "Which language is easy?\n1.Python\n2.Java\n3.C\n4.C++" : 1,
    "Which is the best algorithm for searching an element in the sorted array?\n1.Linear Search\n2.Binary Search\n3.Bubble Sort\n4.topological Sort" : 2,
    "What is the output of following code?\nprint(\"2\"*2)\n1.2\n2.4\n3.22\n4.4" : 3,
    "What is 2^9?\n1.512\n2.18\n3.1024\n4.45" : 1
}
random_questions = []
for key in questions.keys():
    random_questions.append(key)
rd.shuffle(random_questions)
for question in random_questions:
    print(question,end="\n\n")
    user_answer = input("Enter your option : ")
    while(user_answer not in [str(i) for i in range(1,5)]):
        print("Please selecct only options 1 | 2 | 3 | 4!")
        user_answer = input("Enter your option again : ")
        print("\n")
    user_answer = int(user_answer)
    print("\n")
    if(questions[question] == user_answer):
        print("Correct ✅\nGood!",end = "\n\n")
        score = score + 1
    else:
        print("Incorrect ❌")
        print(f"The correct option is {questions[question]}\n")
accuracy = (score / len(questions)) * 100
print(f"Your score is {score} \nAccuracy is {accuracy:.2f}%")
if(accuracy >= 0 and accuracy < 25):
    print("Better Luck!")
elif(accuracy >= 25 and accuracy < 50):
    print("Good!")
elif(accuracy >= 50 and accuracy < 75):
    print("Awesome!")
else:
    print("Excellent!")