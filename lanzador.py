def lanzador():
    eleccion=input("\n\nElige el ejercicio que desea ejecutar: \n 1: Ejercicio Matriz \n 2: Ejercicio Texto \n 3: Ejercicio Listas \n 4: Ejercicio Tabla\n 5: Finalizar el programa\n")
    if eleccion=="1":
        from ejercicios.ejercicio1 import Matriz
        Matriz.crear_matriz()
        lanzador()
    elif eleccion=="2":
        from ejercicios.ejercicio2 import Texto
        Texto.crear_texto()
        lanzador()
    elif eleccion=="3":
        from ejercicios.ejercicio3 import Listas
        print(Listas.crear_lista(0,[], 1, 10))
        print(Listas.crear_lista(-10,[], 2, 20))
        print(Listas.crear_lista(-19,[], 2, -1))
        print(Listas.crear_lista(0,[], 5, 50))
        lanzador()
    elif eleccion=="4":
        from ejercicios.ejercicio4 import Tabla
        Tabla.crear_tabla()
        lanzador()
    elif eleccion=="5":
        exit()
