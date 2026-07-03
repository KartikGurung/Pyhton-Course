import module
#help(module)

n = int(input("Enter Celsius: "))
m = int(input("Enter Fahrenheit: "))

print("Conversion into Fahrenheit :",module.celsius_to_farenheit(n))
print("Conversion into Celsius",module.fahrenheit_to_celsius(m))