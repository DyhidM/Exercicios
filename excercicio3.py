"""
Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while . 
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
"""

# 1
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)
    
# 2
numeros = range(1,21)
for numero in numeros:
    if numero % 2 == 0: 
        print(numero)

 
# 3
numeros = range(1,101)
suma = 0
for i in numeros:
    suma += i
print("La suma es:", suma)
 
