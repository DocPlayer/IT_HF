print('Taschenrechner Menu')
print('Um zu rechnen, geben Sie 1 ein. 0 beendet das Programm')
while input== 1:
    print('Geben Sie zwei Zahlen ein')
    Zahl1 = input("Eingabe")
    Zahl2 = input("Eingabe")
    oparator = input("Eingabe")
    if oparator == '+':
        addiere(Zahl1, Zahl2)
    elif oparator == '-':
        subtrahiere(Zahl1, Zahl2)
    elif oparator == '*':
        multipliziere(Zahl1, Zahl2)
    elif oparator == '/':
        dividiere(Zahl1, Zahl2)
    else:
        print("Gib einen gültigen Oparator an")
    print(Result = zahl)
