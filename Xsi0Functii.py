import random
continua = "Da"
dictionar = {(1, '00'), (2, '01'), (3, '02'), (4, '10'), (5, '11'), (6, '12'), (7, '20'), (8, '21'), (9, '22')}
tablaDeJoc = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
# cu ce incepem
def inceput() -> str:
    if random.randint(0, 1) == 0:
        return 'X'
    else:
        return '0'


# cine incepe
def primul_jucator():
    if random.randint(0, 1) == 0:
        return 'calculator'
    else:
        return 'utilizator'


def initializare_jucatori():
    for i in jucatori.keys():
        if i == primul:
            jucatori[i] = start
    if start == 'X':
        urmator = '0'
    else:
        urmator = 'X'
    for i in jucatori.keys():
        if jucatori[i] == '_':
            jucatori[i] = urmator
    return True


def alegecalculator (x:str, n:int, ok:bool) :
    while ok:
        alege = random.randint(0, 9)
        if int(alege) > 0 and int(alege) < 10:
            for key, value in dictionar:
                if key == int(alege):
                    poz = value
                    if tablaDeJoc[int(poz[0])][int(poz[1])] == '_':
                        tablaDeJoc[int(poz[0])][int(poz[1])] = jucatori[x]
                        n += 1
                        x = 'utilizator'
                        ok = False
                        print(tablaDeJoc[0], f"\n{tablaDeJoc[1]}", f'\n{tablaDeJoc[2]}')
                        return x, n, ok



def alege_utilizator(x:str, n:int, ok:bool):
    while ok:
        alege = input('Selecteaza unde vrei sa pui ' + jucatori[x] + ': ')
        if int(alege) > 0 and int(alege) < 10:
            for key, value in dictionar:
                if key == int(alege):
                    poz = value
                    if tablaDeJoc[int(poz[0])][int(poz[1])] == '_':
                        tablaDeJoc[int(poz[0])][int(poz[1])] = jucatori[x]
                        n += 1
                        x = 'calculator'
                        ok = False
                        print(tablaDeJoc[0], f"\n{tablaDeJoc[1]}", f'\n{tablaDeJoc[2]}')
                        return x, n, ok
                    else:
                        print('Pozitia selectata este deja ocupata, alegeti altceva')
        else:
            print("Alege o alta pozitie, cea selectata anterior nu se gaseste pe tabla de joc")
            print(tablaDeJoc[0], f"\n{tablaDeJoc[1]}", f'\n{tablaDeJoc[2]}')



def castigator() -> str:
    raspuns = 'again'
    for i in range(0, 3):
        if 'X' in tablaDeJoc[i] and not '0' in tablaDeJoc[i] and not '_' in tablaDeJoc[i]:
            print('A castigat "X"')
            raspuns = input('Tastati daca vreti sa continuati ')
            return raspuns
        elif '0' in tablaDeJoc[i] and not 'X' in tablaDeJoc[i] and not '_' in tablaDeJoc[i]:
            print('A castigat "0"')
            raspuns = input('Tastati daca vreti sa continuati ')
            return raspuns
    for i in range(0, 3):
        if tablaDeJoc[0][i] == 'X' and tablaDeJoc[1][i] == 'X' and tablaDeJoc[2][i] == 'X':
            print('A castigat "X"')
            raspuns = input('Tastati daca vreti sa continuati ')
            return raspuns
        elif tablaDeJoc[0][i] == '0' and tablaDeJoc[1][i] == '0' and tablaDeJoc[2][i] == '0':
            print('A castigat "0"')
            raspuns = input('Tastati daca vreti sa continuati ')
            return raspuns
    if tablaDeJoc[0][0] == 'X' and tablaDeJoc[1][1] == 'X' and tablaDeJoc[2][2] == 'X':
        print('A castigat "X"')
        raspuns = input('Tastati daca vreti sa continuati ')
        return raspuns
    elif tablaDeJoc[0][0] == '0' and tablaDeJoc[1][1] == '0' and tablaDeJoc[2][2] == '0':
        print('A castigat "0"')
        raspuns = input('Tastati daca vreti sa continuati ')
        return raspuns
    elif tablaDeJoc[0][2] == 'X' and tablaDeJoc[1][1] == 'X' and tablaDeJoc[2][0] == 'X':
        print('A castigat "X"')
        raspuns = input('Tastati daca vreti sa continuati ')
        return raspuns
    elif tablaDeJoc[0][2] == '0' and tablaDeJoc[1][1] == '0' and tablaDeJoc[2][0] == '0':
        print('A castigat "0"')
        raspuns = input('Tastati daca vreti sa continuati ')
        return raspuns
    return raspuns


def egalitate():
    print('Este egalitate')
    print(tablaDeJoc[0], f"\n{tablaDeJoc[1]}", f'\n{tablaDeJoc[2]}')
    return input('Tastati daca vreti sa continuati ')


while continua == "Da":
    tablaDeJoc = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    mutari = 0
    jucatori ={'calculator': '_', 'utilizator': '_'}
    # cine incepe primul random
    primul = primul_jucator()
    # cu ce se incepe random
    start = inceput()
    initializare_jucatori()
    rand = primul
    while mutari < 9:
        verific = True
        while verific:
            muta = rand
            if rand == 'calculator':
                muta, mutari, verific = alegecalculator(muta, mutari, verific)
            else:
                muta, mutari, verific = alege_utilizator(muta, mutari, verific)
            rand = muta

        # verificare daca a castigat
        iesire = 'again'
        if mutari > 4:
            iesire = castigator()
            print(iesire)
        if iesire != 'again':
            continua = iesire
            break
    #verificare daca e egalitate
    if mutari == 9 and iesire == 'again':
        continua = egalitate()










