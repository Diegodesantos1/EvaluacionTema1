class Listas:
    def __init__(self):
        self.lista1 = list(range(11)) ; self.lista2 = list(range(-10, 1))
        self.lista3 = list(range(0, 22, 2))
    def __str__(self):
        return str(self.lista1) + str(self.lista2)
    def formato_lista(self):
        print(self.lista1) ; print(self.lista2)
        print(self.lista3)


listas = Listas()
print("Listas: {}".format(listas))
listas.formato_lista()



