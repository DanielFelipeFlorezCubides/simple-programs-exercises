# Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
# El promedio del ramo se calcula con la siguiente formula.
# NC=(C1+C2+C3)/3
# NF=NC⋅0.7+NL⋅0.3
# Donde NC
# es el promedio de certámenes, NL
# el promedio de laboratorio y NF
# la nota final.

# Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, 
# y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

# Obtener las notas de los dos primeros certámenes y la nota de laboratorio
nota1 = float(input("Ingrese la nota del primer certamen: "))
nota2 = float(input("Ingrese la nota del segundo certamen: "))
nota_lab = float(input("Ingrese la nota de laboratorio: "))

# Calcular la nota necesaria en el tercer certamen para aprobar con 60
promedioNotas = (60 - (nota_lab * 0.3)) / 0.7
nota_necesaria = round(((3 * promedioNotas) - (nota1 + nota2)) - 2) 

# Mostrar la nota necesaria
print(f"La nota necesaria en el tercer certamen para aprobar con 60 es: {nota_necesaria}")