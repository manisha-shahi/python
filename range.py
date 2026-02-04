students = []

n = int(input("please enter the number you enter student: "))
if n not in [1,2,3,4,5,6]:

    print("wrong value")
else:
    for i in range(n):
        student = {
            "id": int(input("Please enter the id: ")),
            "name": input("Please enter the name: "),
            "address": input("Please enter the address: "),
            "email_id":input("Please enter the email id :")
        }

        students.append(student)

    print("\n--- All Students Details ---")
    for data in students:
        print(data)