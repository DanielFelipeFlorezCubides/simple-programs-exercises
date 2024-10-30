# Cuando un huevo es hervido en agua, las proteínas comienzan a coagularse cuando 
# la temperatura sobrepasa un punto crítico. A medida que la temperatura aumenta, las reacciones se aceleran.

# En la clara, las proteínas comienzan a coagularse para temperaturas sobre 63°C, mientras que en la yema 
# lo hacen para temperaturas sobre 70°C. Para hacer un huevo a la copa, la clara debe haber sido calentada lo 
# suficiente para coagularse a más de 63°C, pero la yema no debe sobrepasar los 70°C para evitar obtener un huevo duro.

# El tiempo en segundos que toma al centro de la yema alcanzar Ty
# °C está dado por la fórmula:

# t= M^2/3 cρ^1/3 / Kπ2(4π/3)^2/3 * ln[0.76To−Tw/Ty−Tw],
# donde M es la masa del huevo, ρ su densidad, c su capacidad calorífica específica y K
# su conductividad térmica. Algunos valores típicos son:

# M=47[g] para un huevo pequeño y M=67[g] para uno grande,
# ρ=1.038[gcm−3], c=3.7[Jg−1K−1], y K=5.4⋅10−3[Wcm−1K−1].
# Tw es la temperatura de ebullición del agua y To la temperatura original del huevo antes de meterlo al agua, ambos en grados Celsius.

# Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida 
# el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

import math

import math

# Constantes
M_pequeño = 47  # Masa del huevo pequeño [g]
M_grande = 67  # Masa del huevo grande [g]
rho = 1.038  # Densidad del huevo [g/cm^3]
c = 3.7  # Capacidad calorífica específica del huevo [J/g*K]
K = 5.4e-3  # Conductividad térmica del huevo [W/cm*K]
Tw = 100  # Temperatura de ebullición del agua [°C]
Ty_max = 70  # Temperatura máxima para la yema [°C]

# Obtener la temperatura original del huevo
To = float(input("Ingrese la temperatura original del huevo (en grados Celsius): "))

# Elegir el tamaño del huevo
tamaño = input("Ingrese el tamaño del huevo (pequeño o grande): ")
if tamaño.lower() == "pequeño":
    M = M_pequeño
elif tamaño.lower() == "grande":
    M = M_grande
else:
    print("Tamaño de huevo inválido.")
    exit()

# Calcular el tiempo en segundos
t = ((M**2 / 3) * (c * rho**(1/3)) / (K * math.pi**2 * (4 * math.pi / 3)**(2/3))) * (math.log((0.76 * To - Tw) / (Ty_max - Tw))) * math.pow(10, -2)

# Mostrar el resultado
print(f"El tiempo para cocinar el huevo a la copa es: {t:.2f} segundos")