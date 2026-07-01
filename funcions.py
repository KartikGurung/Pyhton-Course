# student = ["ram", "raju", "jiya", "priya"]
# def name(*student):
# #    return student
#     print(student)

# name(*student) #-->function call
# print(type(student))


# student = {
#     "name" : "aman",
#     "age" : 22,
#     "class" : "Second"
# }

# def student_info(student):
#     print(student["name"])
#     print(student["age"])
#     print(student["class"])

# student_info(student)

# def get_user():
#     return {
#         "name": "Rahul",
#         "age": 25,
#     }
# print(get_user())

# def create_user(user):
#     return {
#         "name": "Rahul",
#         "age": 25
#     }
# def create_user():
#     print()


# def create_students(students):
#     for students in students:
#         print(students)
# create_students([
#     "Rahul",
#     "Ankit",
#     "Aman"
# ])

# def get_numbers():
#     return [10,20,30,40]
# print(get_numbers())

# def get_student():
#     return {
#         "id":1,
#         "name":"Rahul"
#     }
# print(get_student())


# def add(a,b):
#     print(a+b)
#     return a+b

# x = add(2,3)
# print(x)

# --> Nested Functions :
from unittest import result

from numpy import inner


# def outer():
#     print("it is outer")

#     def inner():
#         print("it is inner")
#     # inner()
#     return inner
# outer()

# --> Global keyword :

z = 99
def fun(y):
    global z 
    z = 20
    # result = fun(x)
    # print(result)

fun(z)
print(z)
