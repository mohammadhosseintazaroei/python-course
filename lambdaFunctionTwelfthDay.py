items = [
    ("product1",10),
    ("product2",30),
    ("product3",5)
]

items.sort(key= lambda item: item[1])
print(items)