class Texto:
    def crear_texto():
        texto = str(input("Escriba el texto que quiera contar: "))
        if len(texto) >= 3 and len(texto) < 10:
            print("\nLa longitud del texto es mayor o igual que 3 y menor que 10 \nTRUE")
        else:
            print("\nLa longitud del texto no es mayor o igual que 3 y menor que 10\nFALSE")