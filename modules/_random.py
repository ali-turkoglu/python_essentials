import random
import math


#result =dir(random)

#result=help(random)

#result=math.floor(random.random()*100)

result=int(random.uniform(1,100))

result=random.randint(1,100)

print(result)


names=["Ali","David","Mike","Daniel"]
print(names[random.randint(0,3)])

result=random.choice(names)
print(result)

liste=list(range(10))
random.shuffle(liste)
print(liste)

liste=range(100)
result=random.sample(liste,3)
print(result)
