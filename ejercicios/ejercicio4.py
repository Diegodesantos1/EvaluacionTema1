class Tabla:
    def crear_tabla():
        print("Introduce las dimensiones de la tabla:")
        filas = int(input("Filas: "))
        columnas = int(input("Columnas: "))
        tabla = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(int(input("Introduzca el elemento ({},{}) de la tabla: ".format(i,j))))
            tabla.append(fila)
        return tabla
    def __init__(self):
        self.tabla = Tabla.crear_tabla()
    def __str__(self):
        return str(self.tabla)
    def formato_tabla(self):
        for i in range(len(self.tabla)):
            for j in range(len(self.tabla[i])):
                print(self.tabla[i][j], end="")
            print()

tabla = Tabla()
print("Tabla: {}".format(tabla))
tabla.formato_tabla()







