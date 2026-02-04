dictdata=[
    {"id":101,"name":"manisha","address":"gurgaon"},
    {"id":102,"name":"tanuja","address":"Hyderabad"},
    {"id":103,"name":"bhanu","address":"UP"}
]
user_name = input("please enter your name :")
found = False 
for data in dictdata:
        if data["name"] == user_name:
            print("the record found successfully : ")
            found = True 
            break
        else:
            print("the record dose not exist :")    