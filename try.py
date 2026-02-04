def user_input():
    id=int(input("please enter student id :"))
    name=input("please enter student name :")

    return (id , name)

def user_output():

    data=user_input()
    print(data)

user_output()