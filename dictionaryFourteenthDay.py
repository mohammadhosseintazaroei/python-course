point = {"x" : 1 ,  "y" :2}
point2 = dict(x = 1, y = 2)
point["x"] = 10
point["z"] = 20
print(point)
del point["z"]
print(point)
print(point["x"])
print(point.get("x"))
print(point2["y"])

for x in point:
    print(x , point[x])
for x in point.items():
    print(x)
for key,value in point.items():
    print(key,value)