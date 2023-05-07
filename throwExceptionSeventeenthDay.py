def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less")
    return 10/age


try:
    print(calculate_xfactor(0))
except Exception as ex:
    print(ex)
