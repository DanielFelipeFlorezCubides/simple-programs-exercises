# Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
# de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
# del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

import math
# Variables declaration input
a = int(input('Give me the lenght of the first side of the triangle: '))
b = int(input('Give me the lenght of the second side of the triangle: '))

# Processing
c = math.sqrt(((a**2)+(b**2)))

# Output
print(f'The hypotenuse of the trinagle is: {c}')