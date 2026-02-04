hindi = int(input("please enter hindi marks :"))
english = int(input("please enter english marks :"))
computer = int(input("please enter computer marks :"))
physics = int(input("please enter physics marks :"))
total = hindi + english + computer + physics
print("total marks = ", total)
percentage = total/4
print("percentage = ", percentage)
if(percentage >= 60):
    print("first division")
elif(percentage >= 45):
    print("II division")
elif(percentage >= 33):
    print("III division")
else:
    print("fail")
