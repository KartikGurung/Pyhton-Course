#Make a calculator

a=(int(input("Enter the value of a: ")))
operator = input("Enter Operator(+, -, *, /): ")
b=(int(input("Enter the value of b: ")))

#Simple Calculator

if operator == "+":
    result = a+b
elif operator == "-":
    result = a-b
elif operator == "*":
    result = a*b
elif operator == "/": 
    if b != 0:
        result = a/b
    else:
        print("Error")
        exit()
else:
    print("Invalid Operator")
    exit()

print("Result: ", result)