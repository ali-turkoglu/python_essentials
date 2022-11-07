numbers=[1,3,6,2,23,54,28]
letters=["s","k","f","o"]

val= min(numbers) #1
val= max(numbers) #54
val= min(letters) #f
val= max(letters) #s
val= numbers[3:6] #2,23,54

numbers[2]=66       #[1, 3, 66, 2, 23, 54, 28]
numbers.append(11)  #[1, 3, 66, 2, 23, 54, 28,11]
numbers.insert(2,333) #[1, 3, 333, 66, 2, 23, 54, 28, 11]

numbers.pop() # delete last element
numbers.pop(1) # delete number of index

numbers.remove(333) # remove given number

numbers.sort()
letters.sort()
numbers.reverse() #reverse in place

val=numbers.count(66) # how many 66 in numbers
val=letters.count("a") #how mamy a in letters

print(val)
print(numbers) 

#---------------------------------------------------------------------

names=["Ali","Ahmet","John","Kane","David"]

index=names.index("John")
names.pop(index)

result="Ahmet" in names # True
# result=names.index("Winsond") # return error -1 -> there is no winsond in the names

names.reverse()
names.clear() # remove all elements in names list

print(names)
print(result) 


# give an element from user and add into a list

cars=[]
car=input("enter a car model : ")
cars.append(car)
car=input("enter a car model : ")
cars.append(car)


print(cars)



