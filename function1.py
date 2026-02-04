students=[]
def student_registration():
   id = int(input("plesae enter your id :"))
   name = input("plesae enter your name :")
   address = input("plesae enter your address:")
   email_id = input("plesae enter your email id :")

   student = {
        "id":id,
        "name":name,
         "address":address,
        "email_id":email_id,
     }
   students.append(student)
   print("***student resistration successfully***")
    

def view_student_data():
    if not students:
        print("student data is not available")
    else:
        print(" student data ")
        for a in students:
            print(a)
   

def search_student_record():
    search_id = int(input("please enter student id :"))
    found =False
    for data in students:
        if data["id"]==search_id:
            print("student record found ")
            print("id :",data["id"]) 
            print("name:",data["name"]) 
            print("address:",data["address"]) 
            print("email_id:",data["email_id"])
            found=True
            break

            if not found:
                print("student not found.") 
            

def exit():
    print("thank you ! program is exited.")

def menu():
    print("1. student registration ")
    print("2. view student data ")
    print("3. search student record")
    print("4. exit ")

    option = input("please enter your option :")
    if option.isdigit():
        pass
    else:
        print("invalid option , only digit")
    return option

def dashboard():
    while True:
        number = menu()
        if number == 1:
            print("**** student registration ****")
            student_registration()
        elif number == 2:
            view_student_data()
        elif number == 3:
            search_student_record()
        elif number == 4:
            exit()
            break
        else:
            print("invalid option.")
    
dashboard()
        
