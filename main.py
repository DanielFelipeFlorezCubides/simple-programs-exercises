# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

def invertir_numero(numero):

  # Verifica si el número tiene tres dígitos
  if 100 <= numero <= 999:

    # Obtiene los dígitos individuales
    centenas = numero // 100
    decenas = (numero % 100) // 10
    unidades = numero % 10

    # Invierte los dígitos
    numero_invertido = unidades * 100 + decenas * 10 + centenas

    return numero_invertido
  else:
    return "The number must has 3 digits."

# Obtiene el número del usuario
numero = int(input("Put a 3 digits number: "))

# Invierte el número y muestra el resultado
numero_invertido = invertir_numero(numero)
print("The inverted number is:", numero_invertido)
