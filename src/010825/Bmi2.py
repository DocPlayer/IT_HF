datenspeicher=[]
def gewichtskontrolle(bmi):
    if bmi>=25:
        print('Übergewicht')
    elif bmi<18.5:
        print('Untergewicht')
    else:
        print('Normalgewicht')
def datenanlegen(person):
    datenspeicher.append(person)
    print(datenspeicher)
def main():
    while True:
        person=[]
        i = 0
        name=input('Name:')
        groesse=float(input('Körpergröße:'))
        gewicht=int(input('Gewicht:'))
        bmi=gewicht/(groesse**2)
        person.append(name)
        person.append(groesse)
        person.append(gewicht)
        person.append(bmi)
        print('BMI :',bmi)
        gewichtskontrolle(bmi)
        datenanlegen(person)
        if input("Beenden? q"):
            break

main()
