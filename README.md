<h1 align="center">Evaluación Inicial</h1>

En este [repositorio](https://github.com/Diegodesantos1/EvaluacionTema1) queda resuelto la Evaluación del Tema 1.

***

<h2 align="center">Parte 1: Ejercicio Matriz</h2>

![image](https://user-images.githubusercontent.com/91721855/191992796-92567c2f-7bae-4828-ac96-0f55bed6078e.png)

```python
class Matriz:
    n= 0
    matriz = []
    def crear_matriz():
        Matriz.n += 1
        if Matriz.n <= 4:
            numero =int(input("Introduce el primer elemento de la fila de la matriz "))
            numero2 =int(input("Introduce el segundo elemento de la fila de la matriz "))
            numero3 =int(input("Introduce el tercer elemento de la fila de la matriz "))
            numero4 = numero + numero2 + numero3
            fila= [numero, numero2, numero3, numero4]
            Matriz.matriz.append(fila)
            Matriz.crear_matriz()
        else:
            print(f"La matriz es:\n\n{Matriz.matriz}")
```

***

<h2 align="center">Parte 2: Operadores Lógicos</h2>

![image](https://user-images.githubusercontent.com/91721855/191992872-24bdd5cc-6ed3-4203-9df4-0b97acea084c.png)

```python
class Texto:
    def crear_texto():
        texto = str(input("Escriba el texto que quiera contar: "))
        numpalabras = len(texto.split())
        if numpalabras >= 3 and numpalabras < 10:
            print("\nLa longitud del texto es mayor o igual que 3 y menor que 10 \nTRUE")
        else:
            print("\nLa longitud del texto no es mayor o igual que 3 y menor que 10\nFALSE")
```

***

<h2 align="center">Parte 3: Operadores Lógicos</h2>

![image](https://user-images.githubusercontent.com/91721855/191992975-e36897d3-832c-494c-bc08-4994f59170ad.png)

```python
class Listas:
    def crear_lista(numinicial, lista, numfinal, limite):
        lista.append(numinicial)
        if numinicial < limite:
            numinicial += numfinal
            Listas.crear_lista(numinicial, lista, numfinal, limite)
            return lista
```

***

<h2 align="center">Parte 4: Tabla</h2>

![image](https://user-images.githubusercontent.com/91721855/191993039-82306d20-a321-4a81-a4e2-6c671c0cab93.png)

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
