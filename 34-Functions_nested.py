def outer(num1):
    print("outer")
    def inner(num1):
        print("inner")
        return num1+1
    return inner(num1)
outer(5)
print(outer(8))