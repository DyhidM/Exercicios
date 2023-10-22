'''
1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” 
o “El número es impar” según corresponda.
'''
def verificar_numero(numero):
  if  numero % 2 == 0:
   return "El numero es par"
  else: 
   return "El numero es impar"
resultado = verificar_numero(5) 
print(resultado)

'''
2. Crea una función a la que pases un número como argumento, calcule el factorial de ese número 
y haga print del resultado.
'''
def factorial(numero):
  resultado = 1
  for i in range(1,numero+1):
    resultado *= i
  return resultado
numero = 5
print("El factorial de",numero,"es:",factorial(numero))


'''
3. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de
“La cantidad de dígitos es:” y el resultado total de dígitos.

'''
def contar_digitos(numero):
 numero_str = str(numero)
 cantidad_digitos = len(str(numero))
 
 return cantidad_digitos
resultado = contar_digitos(456878)

print(f"La cantidad de dígitos es:{resultado}")

'''
 4. Dada una lista de números, crea una función que devuelva el número máximo de la lista.
'''
def numero_max(list):
 maximo = max (list)
 
 return maximo 
numeros = [56,67,80,98,22]
maximo = numero_max(numeros) 
print(f"El numero maximo es:", maximo)

'''
5. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
'''
def suma_digitos(numero):
  numero_str = str(numero)
  suma = 0
  for digito in numero_str:
    suma +=int(digito)
  return suma
resultado = suma_digitos(555)
print("Suma digitos es : ", resultado)

'''
6. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, 
que se les pasarán como argumento a la función, y devuelva el MCM.
'''
def mcm(a,b):
  if a == 0 or b == 0:
    return 0
  else:
    maximo = max(a,b)
    while True:
       if maximo % a == 0 and maximo % b == 0:
         return maximo
       maximo +=1
       
num1 = 5
num2 = 8
print("El MCM es:", mcm(num1,num2))

'''
7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
'''
def area_triangulo(base,altura):
  return base*altura/2
base = 3
altura = 5
resultado = area_triangulo(base,altura)
print("El area del triangulo es:", resultado)

'''
8. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
'''
def verificar_numero(numero):
  if numero < 0:
    return "negativo"
  elif numero > 0:
    return "positivo"
  else:
    "El numero es 0"
resultado = verificar_numero(-65)
print("El numero es:", resultado)

'''
9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
'''
def contar_letras(palabra):
  contador = 0
  for letra in palabra:
    if letra.isalpha():
      contador +=1
  return contador
palabra = "excercicio"
cantidad = contar_letras(palabra)
print(f"La palabra ",{palabra}, "tiene", cantidad, "letras")

'''
 10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
 '''
def valor_absoluto(list_num):
  for i in range(len(list_num)):
   list_num[i] = abs(list_num[i])
  return list_num
numeros = [4,-5,-76,7,89,-54]
absolutos = valor_absoluto(numeros)
print("Lista con valores absolutos",absolutos)

'''
11.Crea una función que, dado un número, verifique si un número es primo.
'''
def es_primo(numero):
  if numero <= 1:
    return False
  for i in range(2,numero):
    if numero % i == 0:
     return False
  return True
if es_primo(2):
 print("El numero es primo")
else:
  print("No es un número primo")
  
'''
12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.
'''
def MCD(a, b):
  while b: 
    a, b = b, a % b
  return a
num1 = 6
num2 = 12  
resultado = MCD(num1,num2) 
print("El MCD es:", resultado)
     
    