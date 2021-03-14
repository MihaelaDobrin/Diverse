# {
#      'Romania': [
#          {
#              'year': '2019',
#              'coverage': 84
#          }, {
#              'year': '2018',
#              'coverage': 67
#          },
#  ..., {
#              'year': '2011',
#              'coverage': 72
#          }
#      ]
# }
# { 'tara':[{'year':'2019', 'coverage':84}, {}], 'tara':[{'year':'2019', 'coverage':84}, {}] }
#

description = ('Country', [
   '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 '
])

dataset = [
   ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
   ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
   ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
   ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
   ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
   ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
   ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
   ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
   ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
   ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
   ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
   ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
   ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
   ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
   ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
   ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
   ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
   ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
   ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
   ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
   ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
   ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
   ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
   ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
   ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
   ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
   ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
   ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
   ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
   ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
   ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
   ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
   ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
   ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
   ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
   ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
   ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
   ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
   ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]


def creare(**kwargs):
    return kwargs


def creare_args(*args):
    return args

lungime = len(description[1])


def creare_lista(n: int) -> list:
    lista = []
    for i in range(0, 9):
        lista.append(creare(year=str(description[1][i]), coverage=str(dataset[n][1][i])))
    return lista


def creare_dictionar() -> dict:
    dictionar_de_lucru = {}
    for i in range(len(dataset)):
        dictionar_de_lucru[dataset[i][0]] = creare_lista(i)
    return dictionar_de_lucru


def get_year_data(dictionar_de_lucru: dict, an: str) -> dict:
    lista_de_lucru = []
    poz_an = description[1].index(an)
    for key, value in dictionar_de_lucru.items():
        lista_de_lucru.append(creare_args(key, value[poz_an]['coverage']))
    dictionar_format = {an: lista_de_lucru}
    return dictionar_format


# {'Romania': [('2019', 84), ('2018', 86), ..., ('2011', 72)]}
def get_country_data(dictionar_de_lucru: dict, tara: str) -> dict:
    lista_de_lucru = []
    valoare = dictionar_de_lucru[tara]
    for i in range(lungime):
        lista_de_lucru.append(creare_args(valoare[i]['year'], valoare[i]['coverage']))
    dictionar_de_lucru = {tara: lista_de_lucru}
    return dictionar_de_lucru


def perform_average(dictionar_country_data: dict):
    contor = 0
    suma = 0
    lista_de_lucru = []
    for key, value in dictionar_country_data.items():
        lista_de_lucru = value
    for i in range(lungime):
        valoare = lista_de_lucru[i]
        if valoare[1] != ': ':
            suma += int(f'{valoare[1][0]}{valoare[1][1]}')
            contor += 1
    if contor == 0 and suma == 0:
        print('Nu s-a putut calcula')
        return 0
    else:
        return round(float(suma/contor), 2)


def main():
    dictionar = creare_dictionar()
    continua = 'Y'
    while continua.upper() == 'Y':
        alegere = int(input('Alegeti ce functie doriti sa apelati: '
                        '1.get_year_data '
                        '2.get_country_data '
                        '3.perform_average '))
        if alegere == 1:
            an_ales = input(f'Alegeti anul pentru care doriti sa se afiseze datele: {description[1]} ')
            print(get_year_data(dictionar, f'{an_ales} '))
        elif alegere == 2:
            tara_aleasa = input('Alegeti tara pentru care doriti sa se afiseze datele: ')
            print(get_country_data(dictionar, tara_aleasa))
        elif alegere == 3:
            tara_aleasa = input('Alegeti tara pentru care doriti sa se afiseze datele: ')
            print(perform_average(get_country_data(dictionar, tara_aleasa)))
        continua = input('Doriti sa fie afisate si alte date: Y/N ')



main()
