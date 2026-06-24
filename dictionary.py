# dict = {
#     "Name" : "john",
#     "Class" : "12th",
#      "Marks" : 75
# }
# dict["Name"] = "kartik"
# print(dict["Name"])
# print(dict["Class"])
# print(dict["Marks"])
# print(dict)
# print(type(dict))
# print(dict[0])

# null_dict = {}
# null_dict["Name"] = "Yaseen"
# print(null_dict)

# Nested Dictionary :

student = {
    "Name" : "Nikhil",
    "Age" : "21",
    "Score" : {
        "OS" : 75,
        "CS" : 80
    }
}
# print(student)
# print(student["Score"]["CS"])
# print(list(student.keys())) #--> Return keys
# print(list(student.values())) #--> Return values
# print(list(student.items())) # --> Return items
# pairs = list(student.items())
# kartik = list(pairs[2][1].items())
# print(kartik[0])
# print(student.get("Name"))
# print(student["Name"])
# print(student)
# student.update({"City" : "Jammu"})
# print(student)
