# Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
centimeter = float(input('Put the centimeters number you want to conver to inches: '))
INCHES = 2.54
conversion = centimeter / INCHES
print(f""" 
    The conversion is: {round(conversion, 1)} in
""")