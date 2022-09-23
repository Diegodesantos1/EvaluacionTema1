class Listas:
    def __init__(self):
        self.lista1 = list(range(11)) ; self.lista2 = list(range(-10, 1))
        self.lista3 = list(range(0, 22, 2)) ; self.lista4 = list(range(-19, 1, 2))
        self.lista5 = list(range(0, 55, 5))
    def formato_lista(self):
        print(self.lista1) ; print(self.lista2)
        print(self.lista3) ; print(self.lista4)
        print(self.lista5)


listas = Listas()
listas.formato_lista()



