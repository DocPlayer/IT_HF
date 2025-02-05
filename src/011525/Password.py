zaehler = 1
eingabe = ''
while (zaehler <=3 and eingabe!='AB123456'):
    print('Passwortabfrage')
    eingabe = input('Passwort:')
    if (eingabe == 'AB123456'):
        print('Es war was war und es kommt was kommt')
    else:
        print('Hallo gehts')
    zaehler = zaehler + 1