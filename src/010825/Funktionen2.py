def rechnen(a,b = 8): # optionaler Parameter b
    print(a*b)
def addieren(a, *b): # b ist eine Liste variabler länge
    erg = a
    for i in b:
        erg +=i
    print(erg)
rechnen(6)
rechnen(6,7)
addieren(6)
addieren(6, 1)
addieren(6, 1, 1)
