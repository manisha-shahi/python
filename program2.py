hindi=int(input("please enter marks in hindi:"))
english=int(input("please enter marks in english:"))
maths=int(input("please enter marks in maths:"))
physics=int(input("please enter marks in physics:"))
computer=int(input("please enter marks in computer:"))

total=hindi+english+maths+physics+computer
print("total marks :", total)
percentage= total/5
print(f"percentage :{percentage}%")
if(percentage>=60):
    print("pass")
else:
    print("fail")    