def lanzador():
    eleccion=input("Elige el ejercicio que desea ejecutar: \n 1: Ejercicio Matriz \n 2: Ejercicio Texto \n 3: Ejercicio Listas \n 4: Ejercicio Tabla ")
    if eleccion=="1":
        from ejercicios.ejercicio1 import Matriz
    elif eleccion=="2":
        from ejercicios.ejercicio2 import Texto
    elif eleccion=="3":
        from ejercicios.ejercicio3 import Listas
    elif eleccion=="4":
        from ejercicios.ejercicio4 import Tabla
lanzador()
