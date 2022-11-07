# map() -> we can pass function and list name to use that function for each element in the list

def square(number): return number**2

numbers=[2,4,5,6,7]

result= list(map(square,numbers))
print(result)
# or
for each in map(square,numbers):
    print(each)


#lambda
 # if we do not use square function, we can use anomious function(noName function)
result2=list(map(lambda number:number**2,numbers))
# or
square=lambda number:number**2
result3=list(map(square,numbers))

# filter() -> return element has only true
def check_Even(num): return num%2==0

result4=list(filter(check_Even,numbers))
print(result4)
# or 
result5=lambda num:num%2==0
print(list(filter(result5,numbers)))