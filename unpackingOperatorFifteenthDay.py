numbers = [1, 2, 3]
name = "mohammad"
values = [*range(5)]
chars = [*"hello"]
print(numbers[0], numbers[1], numbers[2])
print(*name)
print(values)
print(chars)

first = [1,2]
second = [4,5]
both = [*first,3,"dd", *second]
print(both)

firstdic = {"x" :1,"b":3}
seconddic = {"x" :10 , "y" :2}
combined = {**firstdic , **seconddic}
print(combined)