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

Tabla.crear_tabla()



