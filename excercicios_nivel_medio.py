'''
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.
'''
def Fibonacci(n):
   a, b = 0, 1
   for i in range(n):
    print(a, end = ' ')
    a, b = b, a + b
Fibonacci(10)

'''
2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
'''
def divisores(numero):
 divisores = []
 for i in range(1, numero+1):
  if numero % i == 0:
   divisores.append(i)
 return divisores
numero = 10
divisores = divisores(numero)
print(f"Divisores del {numero} son:",divisores)
               
def divisores(n):
  return [i for i in range(1,n+1)if n%i==0]
print(divisores(12))

'''
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
'''
def elementos_unicos(list_original):
   return list(set(list_original))
list_original=[4,4,7,10,10,15,17]
resultado = elementos_unicos(list_original)
print("Lista de elementos unicos:", resultado)

"""
4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
"""
           # solución 1:
def suma_digitos(numero):
   suma = 0
   while numero > 0:
     digito = numero % 10
     suma += digito
     numero //= 10
 
   return suma
numero = 232
result = suma_digitos(numero)
print(f"Suma digitos de numero {numero} es:",result)
             # solución 2:

def suma_digitos(numero):
  total = 0
  for digito in str(numero):
   total += int(digito)  
  return total
numero = 232
suma = suma_digitos(numero)
print("Suma digitos es:",suma )

"""5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
"""
def numero_vocales(cadena):
  vocales = ['a','o','e','i'',u']
  cadena = cadena.lower()
  total = 0
  for caracter in cadena:
    if caracter in vocales:
     total += 1
  return total
cadena = "Hola Power"
vocales = numero_vocales(cadena)
print(f"La cadena {cadena} tiene ", vocales, "vocales")

'''
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
'''
def first_n_elements(list,n):
  return list[:n]
print(first_n_elements([4,5,6,9,11],4))

'''
7. Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
'''
# solución 1
def contar_mayusculas_minusculas(cadena):
  mayusculas = sum(1 for letra in cadena if letra.isupper())
  minusculas = sum(1 for letra in cadena if letra.islower())
  return mayusculas, minusculas
cadena = "HeLLo, PoWer"
cantidad = contar_mayusculas_minusculas(cadena)
print(f"La cadena '{cadena} 'tiene",cantidad,"mayusculas y minusculas")

# solución 2
def contar_letras(cadena):
  mayusculas = 0
  minusculas = 0
  for letra in cadena:
   if letra.isupper():
     mayusculas +=1
   elif letra.islower():
     minusculas += 1
  return mayusculas, minusculas   
cadena = "HeLLo, PoWer"
mayusculas, minusculas = contar_letras(cadena)
print(f"Cantidad de letras mayusculas: {mayusculas}")
print(f"Cantidad de letras minusculas: {minusculas}")

'''
8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. 
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. 
Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
'''
def verificar_numero(num):
  suma = 0
  for divisor in range(1,num):
    if num % divisor == 0:
      suma+=divisor 
  return suma == num
num = 6
perfecto = verificar_numero(num)
if perfecto:
 print(f"Numero {num} es perfecto")
else:
 print(f"El {num} no es un numero perfecto")
  
"""
9. Ejercicio: Define una función que reciba un número y retorne su representación en binario. 
"""
def binario(num):
  return bin(num).replace("0b", "")
num = 13
resultado = binario(num)
print(f"Representacio de {num} en binario:", resultado)

'''
10. Ejercicio: Define una función que reciba dos listas 
y retorne la intersección de ambas (los elementos que están en las dos listas).
'''
def intersection(list1,list2):
  return list(set(list1) & set(list2))
list1 = [3,4,5,4,6]
list2 =[3,3,4,6,7]
resultado = intersection(list1,list2)
print("Lista de intersección es:", resultado) 

'''
11. Define una función que tome una cadena y determine si es un palíndromo 
(se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def es_palíndromo(cadena):
  cadena = cadena.lower().replace(" ", "")
  return cadena == cadena[::-1]
cadena = "Oso"
resultado = es_palíndromo(cadena)
print(resultado)

'''
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” 
en lugar del número y para los múltiplos de cinco imprima “Buzz”. 
Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”. 
'''
def Fizz_Buzz():
 resultados = []
 
 for numero in range(1,51):
   if numero % 3 == 0 and numero % 5 == 0:
    resultados.append("FizzBuzz")
   elif numero % 3 == 0:
    resultados.append("Fizz")
   elif numero % 5 == 0:
    resultados.append("Buzz")
   else:
    resultados.append(numero)
 return resultados
resultado = Fizz_Buzz()
print (resultado)

'''
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada e
n orden ascendente.
'''
def ordenar_ascendente(lista):
    return sorted(lista)
lista_original = [5,36,12,56,4,8]
lista_ordenada = ordenar_ascendente(lista_original)
print(lista_ordenada)
'''
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, 
y retorne la lista de palabras que son más largas que n.
'''
def filtrar_palabras(list_palabras,n):
  palabras_filtradas=[]
  for palabra in list_palabras:
   if len(palabra) > n:
      palabras_filtradas.append(palabra)
  if palabras_filtradas:
   return palabras_filtradas
  else:
   return f"No hay palabras mas largas que {n}"
list_palabras = ['Hello', 'Python', 'Soy', 'Mariia']
n = 4
resultado = filtrar_palabras(list_palabras,n)
print(resultado) 

'''
15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
'''
def Fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  fib = [0,1]
  while len(fib) < n:
    fib.append(fib[-1]+fib[-2])
  return fib
print(Fibonacci(10))

'''
16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
'''
def mayor_numero(list):
  return max(list)
mi_list=[5,8,16,6,26,7]
resultado = mayor_numero(mi_list)
print("El numero mas grande de la lista es:",resultado)

'''
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
'''
def suma_digitos_cubo(n):
 suma = 0
 for digit in str(n):
  suma += int(digit)**3

 return suma
numero = 234
resultado = suma_digitos_cubo(numero)
print(f"Suma dígitos al cubo del numero {numero} es:", resultado)
 
'''
18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
'''
def segundo_max(list):
  return sorted(set(list), reverse = True ) [1]
lista = [45, 4, 8, 87, 34]
resultado = segundo_max(lista)
print('El segundo número más grande de la lista', resultado)

'''
19.Ejercicio: Define una función que tome dos listas y retorne True si tienen al
 menos un miembro en común, de lo contrario, retorne False.
'''
def miembro_comun(list1, list2):
  return bool(set(list1) & set(list2))
l1 =[5,8,2,9]
l2 =[4,5,6,3,10]
resultado = miembro_comun(l1,l2)
print(resultado)

'''
 20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.
'''
def lista_inversa(lista):
  return lista[::-1]
lista_original = [1,2,3,4,5]
resultado = lista_inversa(lista_original)
print(resultado)

'''
21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígi
tos y letras que contiene.
'''
def contar_digitos_letras(cadena):
  contar_letras = 0
  contar_digitos = 0
  for letra in  cadena:
   if  letra.isalpha():
    contar_letras += 1
  for digit in cadena:
    if digit.isdigit():
     contar_digitos += 1
  return contar_letras, contar_digitos
mi_cadena = "Power.2024"
resultado = contar_digitos_letras(mi_cadena)
print (f"La cadena {mi_cadena} tiene",resultado, "letras y digitos")

'''
22. Ejercicio: Define una función que reciba una lista de números y retorne la sum
a acumulada de los números
'''
def suma_acumulada(lista):
  total = 0
  suma_acumulada =[]
  for numero in lista:
    total += numero 
    suma_acumulada.append(total)
  return suma_acumulada
lista_n =[5,6,7,9,10]
resultado = suma_acumulada(lista_n)
print(resultado)
  
'''
  23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
  '''
from collections import Counter
  
def numero_comun(lista):
 return Counter(lista).most_common(1)[0][0]
mi_lista = [3,4,5,6,5,3,5]
resultado = numero_comun(mi_lista)
print("El numero mas común en la lista es:", resultado)

'''
24. Ejercicio: Define una función que tome un número y retorne un diccionario con
 la tabla de multiplicar de ese número del 1 al 10.
'''
  # solucion 1
def diccionario_tabla_multiplicacion(n):
  tabla = {}
  for i in range(1,11):
    tabla[i] = n*i
  return  tabla
num = 5
Tabl = diccionario_tabla_multiplicacion(num)
print(Tabl)

  # solucion 2
def tabla_de_multiplicar(numero):
     return {i: numero * i for i in range(1, 11)}
print(tabla_de_multiplicar(5))

'''
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con
la cantidad de apariciones de cada caracter en la cadena.
'''
def cantidad_caracteres(cadena):
  caracter = {}
  for i in cadena:
    caracter [i] = cadena.count(i)
  return caracter
mi_cadena = "Tengo 30 años."
resultado = cantidad_caracteres(mi_cadena)
print(resultado)

'''
26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
'''
def elementos_differentes(list1,list2):
  return list(set(list1)^set(list2))
mi_lista1 = [5,6,7,7,8,9]
mi_lista2 = [1,2,3,4,5,6]
resultado = elementos_differentes(mi_lista1,mi_lista2)
print(resultado)

'''
27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
'''
def lista_sin_dublicados(lista):
  return list(set(lista))
mi_lista = [4,5,5,7,8,8,9,10,10]
resultado = lista_sin_dublicados(mi_lista)
print(resultado)

"""28. Ejercicio: Define una función que reciba un número entero positivo y retorne 
la suma de los cuadrados de todos los números pares menores o iguales a ese número.
  """
def suma_cuadrados_pares(n):
  suma = 0
  for i in range (2,n+1,2):
   suma += i**2
  return suma 
numero = 6     
resultado = suma_cuadrados_pares(numero)
print(resultado)
 
'''
29. Ejercicio: Define una función que reciba una lista de números y retorne 
el promedio de los números en la lista.
'''    
def promedio_numeros(lista):
  return sum(lista)/len(lista)
mi_lista = [5,6,8,9,10]
promedio = promedio_numeros(mi_lista)
print(promedio)

'''
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
'''
def cadena_mas_larga(lista):
  return max(lista, key=len)
mi_lista = ["Hello", 'Power', 'Python']
resultado = cadena_mas_larga(mi_lista)
print("La cadena mas larga es:", resultado)

'''
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
'''
def numero_es_primo(n):
  if n < 2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

def primeros_primos(n):
  primos =[]
  numero = 2
  while len(primos) < n:
    if numero_es_primo(numero):
      primos.append(numero)
    numero += 1
  return primos
num = 5
lista = primeros_primos(num)
print(f"{num} primeros numeros primos del {num} son:",lista)

'''
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
'''
def invertir_palabras(cadena):
  return ' '.join(cadena.split()[::-1])
mi_cadena = "Hola, ¿como esta?"
resultado = invertir_palabras(mi_cadena)
print(resultado)

'''
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada 
en el último elemento de cada tupla.
'''
def ordenar_por_ultimo_elemento(tuplas):
 return sorted(tuplas, key=lambda x: x[-1])
print(ordenar_por_ultimo_elemento([(1, 4), (3, 1), (4, 8)]))

'''
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
'''
def cantidad_vocales(cadena):
  return sum(1 for letra in cadena.lower() if letra in "aouei")
print(cantidad_vocales("Como estas Power")) 
 
"""35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario
retorne False.
  """
def es_primo(numero):
  if numero < 2:
    return False
  for i in range (2,int(numero**0.5)+1):
    if numero % i == 0:
     return False
  return True
n = 19
resultado = es_primo(n)
print(resultado)