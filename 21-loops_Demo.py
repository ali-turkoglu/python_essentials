import random

number= random.randint(1,10)

live=5
count=0

while live>0:
    live -=1
    count+=1
    guess=int(input("guess a number: "))

    if number==guess:
        print(f"welldone, you find the number your {count}. turn. Total score: {100-(20*(count-1))}")
        break
    elif number<guess:
        print("down")
    else:
        print("up")  

    if live==0:
        print("game over")
