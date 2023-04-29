items = [
    ("product1",10),
    ("product2",30),
    ("product3",5)
]


x = list(filter(lambda item:item[1] >= 10  , items))
print(x)