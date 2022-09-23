# Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

class Listas:
    def __init__(self):
        self.lista1 = list(range(11))
    def __str__(self):
        return str(self.lista1)
    def formato_lista(self):
        print(self.lista1)


listas1 = Listas()
print("Listas: {}".format(listas1))
listas1.formato_lista()
