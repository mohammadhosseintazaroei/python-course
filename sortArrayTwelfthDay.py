numbers = [3,20,1,7,4]

print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(sorted(numbers))
print(numbers)


items = [
    ("product1",10),
    ("product2",30),
    ("product3",5)
]
def sort_item(item):
    return item[1]
items.sort(key=sort_item)
print(items)