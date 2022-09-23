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



