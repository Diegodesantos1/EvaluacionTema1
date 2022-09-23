class Matriz:
    def __init__(self):
        self.matriz = []
        for i in range(4):
            fila = []
            for j in range(3):
                fila.append(int(input("Ingrese el elemento ({},{}) de la matriz: ".format(i,j))))
            fila.append(sum(fila))
            self.matriz.append(fila)
    def __str__(self):
        return str(self.matriz)
    def formato_matriz(self):
        for i in range(4):
            for j in range(3):
                print(self.matriz[i][j], end="")
            print(self.matriz[i][3])

