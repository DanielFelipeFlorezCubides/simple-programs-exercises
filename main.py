# Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

radius = float(input('Give the radius of the circunference please: '))
perimeter = ((radius * 2)* 3.141592)
Area = ((radius**2)*(3.141592))
print(f"""
    The perimeter of the circunference is {round(perimeter,1)}
    The area of the circunference is {round(Area, 1)}
""")