# try:
#     age = int(input("Age: "))
#     print(age)
#     xfactor = 10/age
#     print(xfactor)
# except ValueError as ex:
#     print("Error", ex)
#     print("you have to enter a number for age")
# except ZeroDivisionError as ex:
#     print("Error", ex)
#     print("age cannot be zero")
# else:
#     print("No exception where thrown")
# print("Done")

try:
    file = open("content.txt")
    age = int(input("Age: "))
    print(age)
    xfactor = 10/age
    print(xfactor)
except (ValueError, ZeroDivisionError)as ex:
    print("Error", ex)
    print("you didnt enter a valid age")
else:
    print("No exception where thrown")
finally:
    file.close()
    # بلاک فاینالی چه ارور داشته باشیم چه نداشته باشیم اجرا میشه
print("Done")
