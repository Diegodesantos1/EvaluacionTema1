class Tabla:
    def crear_tabla():
        print("Introduce las dimensiones de la tabla:")
        filas = int(input("Filas: "))
        columnas = int(input("Columnas: "))
        tabla = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(int(input("Ingrese el elemento ({},{}) de la tabla: ".format(i,j))))
            tabla.append(fila)
        return tabla
    def __init__(self):
        self.tabla = Tabla.crear_tabla()
    def __str__(self):
        return str(self.tabla)




