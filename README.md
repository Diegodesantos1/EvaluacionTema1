<h1 align="center">Evaluación Inicial</h1>
---
En este [repositorio](https://github.com/Diegodesantos1/EvaluacionTema1) queda resuelto la Evaluación del Tema 1.

***

<h2 align="center">Parte 1: Ejercicio Matriz</h2>

El código es el siguiente:
```python
class Matriz:
    def crear_matriz():
        n1=int(input("Introduce el elemento (1,1) ")) ; n2=int(input("Introduce el elemento (1,2) "))
        n3=int(input("Introduce el elemento (1,3) ")) ; n4=int(input("Introduce el elemento (2,1) "))
        n5=int(input("Introduce el elemento (2,2) ")) ; n6=int(input("Introduce el elemento (2,3) "))
        n7=int(input("Introduce el elemento (3,1) ")) ; n8=int(input("Introduce el elemento (3,2) "))
        n9=int(input("Introduce el elemento (3,3) "))
        n10= n1 + n2 + n3 ; n11 = n4 + n5 + n6 ; n12 = n7 + n8 + n9
        fila1= [n1,n2,n3, n10] ; fila2= [n4, n5, n6, n11] ; fila3 = [n7,n8,n9, n11]
        print(f"La matriz es:\n\n{fila1}\n{fila2}\n{fila3}")
```

***

<h2 align="center">Parte 2: Operadores Lógicos</h2>

El código es el siguiente:
```python
class Texto:
    def crear_texto():
        texto = str(input("Escriba el texto que quiera contar: "))
        if len(texto) >= 3 and len(texto) < 10:
            print("\nLa longitud del texto es mayor o igual que 3 y menor que 10 \nTRUE")
        else:
            print("\nLa longitud del texto no es mayor o igual que 3 y menor que 10\nFALSE")
```

***

<h2 align="center">Parte 3: Operadores Lógicos</h2>

```python
class Listas:
    def crear_lista():
        lista1 = list(range(11)) ; lista2 = list(range(-10, 1)) ; lista3 = list(range(0, 22, 2))
        lista4 = list(range(-19, 1, 2)) ; lista5 = list(range(0, 55, 5))
        print("Las listas son las siguientes:")
        print(lista1) ; print(lista2) ; print(lista3) ; print(lista4) ; print(lista5)
```

***

<h2 align="center">Parte 4: Tabla</h2>

```python
class Tabla:
    def crear_tabla():
        filas = int(input("Introduce el número de filas "))
        columnas = int(input("Introduce el número de columnas "))
        if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
                print("Número no válido")
        else:
            for i in range(filas):
                print("")
                for j in range(columnas):
                    print(" * ", end ='')
```

***

<h2 align="center">Parte 5: Codewars</h2>

![image](https://user-images.githubusercontent.com/91721855/191952640-9c135519-1de9-4974-ab6a-c4cad2295c76.png)

El código es el siguiente:
```python
def string_to_array(s):
    if s == '' or "":
        return [""]
    else:
        return s.split()
```
