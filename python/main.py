import random
def BinarySeach(Dato, listaOrdenada):
    Flag = True
    B = len(listaOrdenada)-1
    A = 0
    
    while Flag:
        if listaOrdenada[int(B-(B - A)/2)] > Dato:
            B = B - int((B - A)/2)
        else:
            A = int(B-(B - A)/2)
        if listaOrdenada[int(A+((B - A)/2))] < Dato:
            A =  A + int((B - A)/2)
        else:
            B = int(A+((B - A)/2))

        if listaOrdenada[B] == Dato:
            Flag = False

        
    return B

def TicTok():
    Gane = False
    Numeros = []
    for i in range(100):
        Numeros.append(i+1)
    Intento = 0
    Numero = random.randint(1,100)
    print("Piensa un Numero del 1 al 100")
    print("Tu Numero es ==> " + str(Numero))
    while Intento < 6:
        Index = BinarySeach(Numero, Numeros)
        Entrada = input("Mayor (W) Menor (S) Es Este (A): ")
        if Entrada.upper() == "A":
            Gane = True
            Intento = 6
        elif Entrada.upper() == "W":
            Numeros = Numeros[Index:]
        elif Entrada.upper() == "S":
            Numeros = Numeros[:Index]
        
        Intento += 1
        Numero = Numeros[int(len(Numeros) / 2)]
        print("Tu Numero es ==> " + str(Numero))
    if not Gane:
        Entrada = input("Mayor (W) Menor (S) Es Este (A): ")
        if Entrada.upper() == "A":
            Gane = True
    if Gane:
        print("=>Yo Gane<=")
    else:
        print("=>Tu Ganas<=")

    





TicTok()

# 

# Index = BinarySeach(4, Numeros)
# print(Index)