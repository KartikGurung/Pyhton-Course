"""Convert temperature b/w Celsius and Fahrenheit"""
# functions :
def celsius_to_farenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius*9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit-32)*5/9

#Constants
FREEZING_PINT_CELSIUS = 0
FREEZING_PINT_FAHRENHEIT = 32
BOILING_POINT_CELSIUS = 100
BOILING_POINT_FAHRENHEIT = 212

