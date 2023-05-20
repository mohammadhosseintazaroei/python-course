from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less")
    return 10/age

try:
    print(calculate_xfactor(0))
except Exception as ex:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calculate_xfactor(0)
if xfactor == None:
    pass

"""

print("code1",timeit(code1,number=10000))
print("code2",timeit(code2,number=10000))
