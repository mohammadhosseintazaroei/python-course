try:
    with open("content.txt") as file,open("another.txt") as target: 
        print(file.read())
        print(target.read())
        print("file opened")
    age = int(input("Age: "))
    print(age)
    xfactor = 10/age
    print(xfactor)
except (ValueError, ZeroDivisionError)as ex:
    print("Error", ex)
    print("you didnt enter a valid age")
else:
    print("No exception where thrown")
print("Done")
