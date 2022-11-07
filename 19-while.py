from operator import le


x=0

while x<=100:
    if x%2==0:
        print(f"{x} is even number")
    x+=1
print("finished")    


name="" # if it is null it means False
while not name.strip():
    name=input("enter your name: ")
print(f"Hello {name}")


numbers=[1,23,33,47,58,56]
i=0
while (i<len(numbers)):
    print(numbers[i])
    i+=1


#store 5 numbers from the user
nums=[]
i=0
while i<5:
    nums.append(int(input("enter a number: ")) )
    i+=1
print(nums.sort())    