s="www www Hello world. Are you there!"
s=s[:6]+"W"+s[7:]
print(s)
s.replace("w","W")

print("abc "*3)

s.upper()        #  upperCase
s.capitalize()   #  capitalize
s.lower()        #  lowerCase  
s.title()       # just upper first letters 

s.strip()        # strip
s.lstrip()        # strip just left
s.rstrip()        # strip just right
s.strip("w.")    # delete all w and .
s.split()        # split
s.split(".")
s1=" ".join(s)  # join s array with space char
s.find("Are")   # find Are work in s and return first char index. if there is not return -1
s.rfind("Are")  # start searching from right side
s.startswith("H") # return true

s.replace("you","we") # change
s.replace("you","we",2) # change first 2 word


s.count("a")  # count a letter
print(s.count("www",0,10)) # is there www from index 0 to index 10, return 1 or 0

s.isdigit()
"deneme".isalpha()

print("Ali".center(50,"*")) #  ***********************Ali************************
"Ali".ljust(50,"*")
