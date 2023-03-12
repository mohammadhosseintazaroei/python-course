def multiply(x, y, z):
    return x * y * z


print(multiply(3, 3, 3))


def multiply_args(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply_args(3, 4, 3,2))
