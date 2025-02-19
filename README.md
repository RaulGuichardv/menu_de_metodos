# Menu de metodos 

proyecto de la  materia de topicos de programacion 


## Metodos :
* Anagrama
```
def anagrama(txt1: str, txt2: str):
    if len(txt1) != len(txt2): return False
    return sorted(txt1.lower()) == sorted(txt2.lower())
 
```
* Invertir cadena
```
def invertir_cadena(txt: str):
    return txt[::-1] 
```
* Fibonacci
```
def fibonacci(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
```
* Eliminar duplicados 
```
def eliminar_duplicador(array: list):
    return list(set(array))
 
```
* Palindromo
```
def palindromo(letter: str):
    letter = letter.replace(" ", "")
    return letter == letter[::-1]
```
* Contar paladras
```
def contar_paladras(text: str):
    array = text.lower().split()
    dict = {}
    for letter in array:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict
 
```
* Encontrar el mayor elemento
```
def encontrar_el_mayor_elemento(array: list):
    return max(array)
```
* Invertir una lista
```
def invertir_una_lista(array: list):
    return array[::-1] 
```
* Filtrar numeros pares
```
def filtrar_numeros_pares(array: list):
    return [num for num in array if (num % 2) == 0]
 
```
* Encontrar el segundo mayor
```
def encontrar_el_segundo_mayor(array: list):
    array.sort(reverse=True)
    return array[1]
 
```
* Contar vocales
```
def contar_vocales(text: str):
    vocales = "aeiou"
    contador = 0
    for letter in text:
        if letter in vocales:
            contador += 1
    return contador
 
```
* Ordenar una lista de tuplas 
```
def ordenar_una_lista_de_tuplas(array: list):
    return sorted(array, key=lambda x: x[1])
 
```
* Contar Caracteres unicos
```
def contar_caracteres_unicos(text: str):
    return len(set(text))
```
* Encuentra palabras mas largas
```
def encuentra_palabras_mas_largas(text: str, num: int):
    letter = text.split()
    letter.sort(key=len, reverse=True)
    return letter[::num]
 ```
* Encontrar numeros primos
```
def es_primo(n: int):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_hasta(n: int):
    primos = []
    i = 2
    while len(primos) < n:
        if es_primo(i):
            primos.append(i)
        i += 1
    return primos
```
