'''
Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''

# 1
numero = 6
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo") 
else: 
    print("El numero es cero")

# 2
numero = 5
if numero % 2 == 0:
    print("El numero es par")
else: numero % 2!= 0
print("El numero es impar")

numeros = [35, 45, 80]
mayor = max(numeros)
print(f"El mayor numero es: {mayor}")