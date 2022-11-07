# key - value

cities=["istanbul","ankara"]
plates=[34,6]

plates={34:"istanbul",41:"kocaeli",33:"mersin"}
print(plates[34]) #istanbul

plates[6]="ankara"

print(plates)

#------------------------------------------

names={
    "Ali":{
        "age":23,
        "phone":"23423523",
        "email":"ali@gmail.com",
        "roles":["user","admin"]
    },
    "Sadık":{
        "age":23,
        "phone":"23423523",
        "email":"ali@gmail.com",
        "roles":["user"]
    }
}

print(names["Ali"]["age"])
print(names["Sadık"]["roles"])
print(names)