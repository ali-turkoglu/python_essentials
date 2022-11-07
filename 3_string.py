firstName="Mehmet"
lastName="Ural"
age=33

str=firstName+" "+lastName+" is "+str(age)+" years old."
print(str)

print(str[0]) #M

length=len(str)
print(length) #28
print(str[length-1]) #last index of str

print(str[-1]) # last char of str

subString=str[0:2] # from 0 to 2, except 2 
subString2=str[7:] # from 7 to end
print(subString)
print(subString2)

print(str[::1]) #print whole chars
print(str[::-1])#print whole chars from end to first
print(str[::2])#print one char from each two
print(str[::3])#print one char from each three

numbers= "12345"*6
print(numbers[::5]) # 11111 -> print every 5. numbers

s="Hello world. Are you there!"
s=s[:6]+"W"+s[7:]
print(s)
s.replace("w","W")

print("abc "*3)

s.upper()        #  upperCase
s.capitalize()   #  capitalize
s.lower()        #  lowerCase  
s.strip()        # strip
s.split()        # split
s.split(".")
s1=" ".join(s)  # join s array with space char
s.find("Are")   # find Are work in s and return first char index. if there is not return -1
s.startswith("H") # return true
s.replace("you","we") # change

