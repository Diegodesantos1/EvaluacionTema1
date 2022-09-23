class Matriz:
    def crear_matriz():
        n1=int(input("Introduce el elemento (1,1) ")) ; n2=int(input("Introduce el elemento (1,2) "))
        n3=int(input("Introduce el elemento (1,3) ")) ; n4=int(input("Introduce el elemento (2,1) "))
        n5=int(input("Introduce el elemento (2,2) ")) ; n6=int(input("Introduce el elemento (2,3) "))
        n7=int(input("Introduce el elemento (3,1) ")) ; n8=int(input("Introduce el elemento (3,2) "))
        n9=int(input("Introduce el elemento (3,3) "))
        n10= n1 + n2 + n3 ; n11 = n4 + n5 + n6 ; n12 = n7 + n8 + n9
        fila1= [n1,n2,n3, n10] ; fila2= [n4, n5, n6, n11] ; fila3 = [n7,n8,n9, n11]
        print(f"La matriz es {fila1}, {fila2}, {fila3}")



