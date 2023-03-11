number = 100

while number > 0:
    print(number)
    number //= 2
print("Done")

command = ""
# first way
# while command.lower() != "exit":
#     command = input(">>>")
#     print(command)
# second way
while True:
    command = input(">>>")
    print(command)
    command.lower() == "exit"
    break