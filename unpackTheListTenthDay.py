numbers = [1, 2, 3, 4, 5, 6]
first = numbers[0]
second = numbers[1]
third = numbers[2]
print(first, second, third)

unpackFirst, unpackSecond, unpackThird, *other = numbers
print(unpackFirst, unpackSecond, unpackThird, other)

unpackFirst,  *other,unpackLast = numbers
print(unpackFirst,other,unpackLast)
