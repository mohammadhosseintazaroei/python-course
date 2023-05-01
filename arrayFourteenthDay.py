from array import array

numbers = array("i", [1, 2, 3])

print(numbers)
print(type(numbers))

numbers.append(1)
print(numbers)

print(numbers[1])
numbers[1] = 3
print(numbers[1])
