class Texto:
    def __init__(self):
        self.texto = input("Escriba el texto que quiera contar: ")
    def __str__(self):
        return self.texto
texto1 = Texto()
print("Texto: {}".format(texto1))
