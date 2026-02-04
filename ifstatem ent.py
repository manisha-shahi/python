student_details=[
{
"102" :{
"name":"manisha shahi",
"qulification":{
"course":'bsc',
"qulification year":2025,
},
"email_id":"shahimanu8@gmail.com",
}},
{
"103":{
"name":"divya shahi",
"qulification":{ 
"course":"m.com",
"qulification year":2025,
}},
"email_id":"divyashahi555@gmail.com",
},
{
"104":{
"name":"tanuja shahi",
"qulification":{ 
"course":"llb",
"qulification year":2024,
},
"email_id":"tanushahi99@gmail.com",
}},
]

student_id=int(input("please enter student id:"))
if (student_details == student_id):
    print(student_details[student_id]["name"])
    print(student_details[student_id]["qulification"])
    print(student_details[student_id]["email_id"])
else:
    print("invalid")
