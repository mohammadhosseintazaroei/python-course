numbers = [1, 1, 2, 3, 4]

first = set(numbers)
print(first)

second = {1, 5, 6}
second.add(4)
second.add(0)
second.remove(5)
print(second)
print(len(second))

print(first | second)  # اجتماع - ادقام عنصر های هر دو مجموعه
print(first & second)  # اشتراک - عنصر های مشترک هر دو مجموعه
# دیفرنس - اختلاف - اعضایی از مجموعه اول که در مجموعه دوم وجود ندارند
print(first - second)
print(first ^second) #سمنتیک دیفرنس - عناصری هستند که یا در مجموعه اول هستند یا دوم ولی در هر دوتاشون نیست

if 10 in first:
    print("yes")
else:
    print("no")
    