hindi= input("please enter hindi marks:")
hindi =int(hindi)
english= input("please enter english marks:")
english = int(english)
computer= input("please enter computer marks:")
computer = int(computer)
maths= input("please enter maths  marks:")
maths = int(maths)
physics= input("please enter physics marks:")
physics =int(physics)
total = hindi+english+computer+maths+physics
percentage= (total /500)*100
print("total marks :", total)
print(f"percentage :{percentage}%")