import random
r = random.randint(0,100)

print("Enter your guess: ")
while(True):
    n = int(input())
    if n>r:
        print("wrong guess,try a smaller number.") 
    elif n<r:
        print("wrong guess.try a larger number.")
    else:
        print("your guess was correct.")
        break