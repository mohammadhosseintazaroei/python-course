def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print("start")
print(multiply(3,3,2))