'''
Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Define una función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
'''

# 1
def suma(a,b):
   return a + b
S = suma(20,25)
print (S)

# 2
def factorial(n):
    if n == 0:
        return(1)    
    else: return n * factorial(n-1)
    
print(factorial(3))

# 3
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
     if numero % i == 0:
         return False
     return True
print(es_primo(111))

# 4
def suma(list):
 total = 0
 for numero in list:
  total += numero    
 return total
print(suma([40,56,70,35]))

def suma_numeros(list):
    return suma(list)
print(suma_numeros([40,56,70,35]))

# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
def cadena_reversa(cadena):
    return cadena[::-1]
print(cadena_reversa("Power school"))
