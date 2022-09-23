class Listas:
    def crear_lista(numinicial, lista, numfinal, limite):
        lista.append(numinicial)
        if numinicial < limite:
            numinicial += numfinal
            Listas.crear_lista(numinicial, lista, numfinal, limite)
            return lista




