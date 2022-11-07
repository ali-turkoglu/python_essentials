numbers=[x for x in range(10)]
print(numbers)


numbers2=[x*x for x in range(10) if x%3==0] # save x if it is dividable 3 into the numbers2
print(numbers2)

str="Hello"
newStr=[x for x in str]
print(newStr)  #['H', 'e', 'l', 'l', 'o']


result=[x if x%2==0 else "TEK" for x in range(1,10)]
print(result)

result2=[(x,y) for x in range(3) for y in range(4)]
print(result2) 
#[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
