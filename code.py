nums=[2,4,0,6,5,9]
print(f"{nums}\n chose any one no from above list")
score=0
import random #it is module in python

def get_guess():
    while True:
        value = input("guess the value: ").strip()
        if value == "":
            print("Please enter a number.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Enter an integer.")

for round in range(3):#loop for 3 rounds
    computers_choice=random.choice(nums)#random,choice indicates the computer will choose anyone no from the list
    print(f"round,{round+1}/3")
    guess_correctly=False
    for chance in range(2):#loop for two rounds
        print(f"chance,{chance+1}/2")
        guess = get_guess()
        if guess==computers_choice:
            guess_correctly=True
            print("correct guess")
            score+=10
            break
        elif guess>computers_choice:
           print("oops!!\n your guess is too high")
        else:
            print("your guess is too low")
    if not guess_correctly:
        print("you lost the round ")
        print("the correct answer was",computers_choice)
        score=max(0,score-5)
print("the final score is=",score)
if score==30:
    print("thats a sharp guess")
elif score>10:
    print("print thats great!!")
else:
    print("better luck next time")
    