# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario

def obtener_parte_decimal(numero):

  parte_entera = int(numero)
  parte_decimal = numero - parte_entera
  return parte_decimal * (1 if numero >= 0 else -1)

# Solicita al usuario que ingrese un número real
numero = float(input("Give me a real number: "))

# Llama a la función para obtener la parte decimal
parte_decimal = obtener_parte_decimal(numero)

# Imprime la parte decimal
print("The decimal of the number is:", parte_decimal)