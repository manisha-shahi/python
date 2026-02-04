students = []
while True:
    student_number=int(input("Please enter the number you went register :" ))
    if student_number<=1 or student_number<=5:
        break 
    else:
        ("wrong value ! Please try agian ...")

for data in range(student_number):

    while True:
        id = input("please enter your id :")
        if(id.isdigit()) :
            break
        else:
            print("invalid id ! only digit allowed:")
    while True:
        name = input("please enter your name :")
        if (name.isalpha()):
            break
        else:
            print("invalid name ! only alphabets allowed:")
    while True:
        address = input("please enter your address :")
        if (address.isalpha()):
            break
        else:
            print("invalid address! only alphabets allowed:")
    while True:
        email_id = input("please enter your email id :")
        if (email_id == '@' and email_id == "."):
            break
        else:
            print("invalid email id !")
    student = {
    "id": int(input("Enter id: ")),
    "name": input("Enter name: "),
    "address": input("Enter address: ")
     }

    students.append(student)
print("\n--- All Students Details ---")
for data in students:
     print(data)
 
 


