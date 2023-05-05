# numbers = [1,2]
# print(numbers[2])
try:
    age = int(input("Age: "))
    print(age)
except ValueError as ex:
    print("Error", ex)
    print("you have to enter a number for age")
else:
    print("No exception where thrown")
print("Done")
