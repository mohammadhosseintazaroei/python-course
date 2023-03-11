def greet(first_name):
    print(f"hi {first_name}")


def getUserInfo(UserInfo):
    return UserInfo


data = getUserInfo(["mohammad", "tazaroie", 16])
file_data = getUserInfo("hey file data")
print(data)
default_path = "./SeventhDayFiles/"
file = open(f"{default_path}content.txt", "w")
file.write(str(data))

second_file = open(f"{default_path}secondFile.txt", "w")
second_file.write(file_data)

def write_file():
    file_name = input("file_name :")
    data = input("data :") 

    file = open(f"{default_path}{file_name}.txt", "w")
    file.write(str(data))

write_file()