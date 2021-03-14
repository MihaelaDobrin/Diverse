lista = ['palarie', 'restaurant', 'apartament', 'parametru', 'mere']


def selectare_cuvant() -> str:
    a = input('Alegeti pozitia unui cuvant din lista: ')
    return lista[int(a)]


def initializare_cuvant(cuvant_ales: str ) ->(list, str) :
    """
    :param cuvant_ales: ce cuvant se foloseste pt joc
    :return: la ce forma s-a ajuns, sirul de litere verificate
    """
    cuvant_format = list(cuvant_ales)
    lungime = len(cuvant_ales)
    for i in range(lungime):
        cuvant_format[i] = '_'
    cuvant_format[0] = cuvant_ales[0]
    cuvant_format[-1] = cuvant_ales[-1]
    for i in range(1, lungime - 2, 1):
        if cuvant_format[0] == cuvant_ales[i]:
            cuvant_format[i] = cuvant_ales[i]
        elif cuvant_format[lungime - 1] == cuvant_ales[i]:
            cuvant_format[i] = cuvant_ales[i]
    litere_verificate = cuvant_ales[0]+cuvant_ales[lungime-1]
    return  cuvant_format, litere_verificate

def desenare_spanzuratoare(incerc:int):
    stadiu = [   """
                    ---------
                    |       |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                 """,
                 """
                    ---------
                    |       |
                    |       0
                    |
                    |
                    |
                    |
                    |
                 """,
                 """
                    ---------
                    |       |
                    |       0
                    |       |                    
                    |
                    |
                    |
                 """,
                 """
                    ---------
                    |       |
                    |       0
                    |       |     
                    |      / 
                    |
                    |
                    |
                 """,
                 """
                 ---------
                 |       |
                 |       0
                 |       |     
                 |      / \\
                 |       
                 |
                 |
                 """,
                 """
                 ---------
                 |       |
                 |       0
                 |       |     
                 |      /|\\
                 |       |
                 |
                 |               
                 """,
                 """
                 ---------
                 |       |
                 |       0
                 |       |     
                 |      /|\\
                 |       |
                 |      /
                 |          
                 """,
                 """
                 ---------
                 |       |
                 |       0
                 |       |     
                 |      /|\\
                 |       |
                 |      / \\
                 |                
                 """
    ]
    return stadiu[incerc]

def alegere_litera():
    alege = input("Alegeti o litera : ")
    return alege

def verificare_litera( litera: str, sirlitere: str,  cuvant_alegere: str, cuvant_formare: list):
    if litera in cuvant_alegere :
        for i in range(len(cuvant_alegere)-1):
            if cuvant_alegere[i] == litera:
                cuvant_formare[i] = litera
        sirlitere += litera
        print("Litera aleasa se gaseste in cuvant")
        return '0', sirlitere, cuvant_alegere, cuvant_formare
    else:
        print('Litera selectata nu se afla in cuvant! Mai incercati')
        sirlitere += litera
        return '1', sirlitere, cuvant_alegere, cuvant_formare


def rejucati() -> bool:
    joc = input("Vreti sa mai jucati o data? ")
    if joc.upper() == "DA":
        return True
    else:
        return False


def joc() -> bool:
    incercari = 0
    cuvant_ales = selectare_cuvant()
    cuvant_format, litere_verificate = initializare_cuvant(cuvant_ales)
    print(cuvant_format)
    while incercari < 7:
        alegere = alegere_litera()
        if alegere in litere_verificate:
            print('Alegeti o alta litera, aceasta a mai fost incercata')
        else:
            crestere, litere_verificate, cuvant_ales, cuvant_format = verificare_litera(alegere, litere_verificate, cuvant_ales, cuvant_format)
            if crestere == '1':
                incercari += 1
                print(desenare_spanzuratoare(incercari))
            print(cuvant_format)
        if cuvant_format == list(cuvant_ales):
            print('Ati castigat!!! Cuvantul ales este ' + str(cuvant_ales))
            return rejucati()
    if incercari == 7:
        print('Ati pierdut!!!')
        return rejucati()


reluare = True
while reluare is True:
    reluare = joc()
