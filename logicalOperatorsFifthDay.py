high_income = False
good_cerdit = False
student = False
#and
#or
#not
if not student and (good_cerdit or not high_income):
    print("Eligible")
else:
    print("not Eligible")