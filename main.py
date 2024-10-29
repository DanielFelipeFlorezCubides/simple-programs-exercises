# Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
firstGrade = float(input('Enter the first grade: '))
secondGrade = float(input('Enter the second grade: '))
thirdGrade = float(input('Enter the third grade: '))
fourthGrade = float(input('Enter the fourth grade: '))
sumAverageGrade = (((firstGrade)+(secondGrade)+(thirdGrade)+(fourthGrade)) / 4)
print(f"""
    The next one is the average grade: {sumAverageGrade}
""")