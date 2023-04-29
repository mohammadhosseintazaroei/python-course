items = [
    ("product1", 10),
    ("product2", 30),
    ("product2", 5),
]

mapCom = list(map(lambda item: item[1], items))
mapCom = [item[1] for item in items if item[1] >=10]
print(mapCom)

filterCom = list(filter(lambda item: item[1] >= 10, items))
filterCom = [item for item in items if item[1] >= 10]
print(filterCom)

