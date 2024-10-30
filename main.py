# Escriba un programa que pregunte al usuario la hora actual t del reloj y 
# un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

# Variables declaration input
t = int(input('Put the current hour: '))
h = int(input('Put the number of hours you want to go to the future: '))
result = t + h

# Processing and output
if result < 12:
    print(f'In {h} hours the clock will show: {result}')
else:
    result = ((t + h)%12)
    print(f'In {h} hours the clock will show: {result}')