class Texto:
    def crear_texto():
        texto = str(input("Escriba el texto que quiera contar: "))
        numpalabras = len(texto.split())
        if numpalabras >= 3 and numpalabras < 10:
            print("\nLa longitud del texto es mayor o igual que 3 y menor que 10 \nTRUE")
        else:
            print("\nLa longitud del texto no es mayor o igual que 3 y menor que 10\nFALSE")