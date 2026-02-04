students =[]
while True:
    print("1. registration")
    print("2. search student record")
    print("3. exit ")
    choice = int(input("please enter your choice :"))
    if choice == 1:
        id = input("enter student id :")
        name = input("enter student name :")
        address = input("enter student address:")
        email_id = input("enter student email id :")

        student ={
            "id": id,
            "name": name,
            "address": address,
            "email_id": email_id
        }
        students.append(student)
        print("student registered successfully.")
    elif choice == 2:
        search_id = input("please enter student id :") 
        found = False
        for data in students:
            if data ["id"] == search_id:
                print("student record found ")
                print("id :", data['id'])
                print("name:", data['name'])
                print("address :", data["address"])
                print("email_id:", data["email_id"])
                found = True
                break

                if not found:
                    print("student record not found ")
    elif choice == 3:
        print("program exited")
        break
    else:
        print("invaild choice, try agian")