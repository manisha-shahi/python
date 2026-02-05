x=int(input("please enter the number :"))
y=int(input("please enter the number :"))

def menu():
    print("***** menu *****")
    print("1. add ")
    print("2. subtaract ")
    print("3. multiply ")
    option=int(input("please enter your option :"))
    return option

def user_input():
    while True:
        number = menu()
        if number==1:
            print("add : ",x+y)
        elif number==2:
            print("subtaract :",x-y)
        elif number==3:
            print("multiply : ",x*y)
        else:
            print("invalid option !")
            break

user_input()
