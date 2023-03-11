successful = False
for number in range(3):
    print("attempt")
    if number == 1:
        successful = True
    if successful:
        print("successful")
        break
    # successful = True
else: 
    print("attempt 3 times and failed")
