x = int(input("please enter the number:"))
y = int(input("please enter the number:"))

def multiply(x,y):
    print("multiply:",x*y)

def division(x,y):
    print("division:",x/y)

def menu():
    print("1.multiply ")
    print("2.division ")
    option = int(input("please enter your option:"))
    return option

def selection():
    number = menu()
    if number == 1:
        multiply(x,y)
      
    elif number == 2:
        division(x,y)
    
selection()
