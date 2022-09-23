class Texto:
    def __init__(self):
        self.texto = input("Escriba el texto que quiera contar: ")
    def __str__(self):
        return self.texto
    def longitud_texto(self):
        if len(self.texto) >= 3 and len(self.texto) < 10:
            print("\nLa longitud del texto es mayor o igual que 3 y menor que 10 \n TRUE")
        else:
            print("\nLa longitud del texto no es mayor o igual que 3 y menor que 10\n FALSE")

