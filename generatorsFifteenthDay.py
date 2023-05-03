from sys import getsizeof
values = (x*2 for x in range(100000))
values2 = {x*2 for x in range(100000)}
values3 = [x*2 for x in range(100000)]

# print(values)
# for x in values:
#     print(x)

print("getnerator", getsizeof(values))
print("getnerator", getsizeof(values2))
print("getnerator", getsizeof(values3))
