message = "z"


def greet(name):
    message = "a"


def send_email(name):
    message = "b"

send_email("mmd")
print(message)




message2 = "p"


def greet2(name):
    global message2
    message2 = "b"


greet2("mmd")
print(message2)