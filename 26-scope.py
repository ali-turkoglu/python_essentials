# assigning global and local variables

x="global x"

def function():
    x="local x"
    print(x)

function()
print(x)    

# global
#  if we want to use global variable in function we can write global keyword and name of variable before using 
num=50
def test():
    global num
    num=20
test()    
print("num=", num)

