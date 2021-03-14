import random


class Tabla:
    dictionar = [{'1': '00'}, {'2': '01'}, {'3': '02'}, {'4': '10'}, {'5': '11'}, {'6': '12'}, {'7': '20'}, {'8': '21'}, {'9': '22'}]

    def __init__(self):
        self.tablaDeJoc = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]
        self.jucatori = {'calculator': '_', 'utilizator': '_'}
        self.muta = None
        self.mutari = 0
        self.verific = True
    # cu ce incepem

    @staticmethod
    def inceput():
        if random.randint(0, 1) == 0:
            return 'X'
        else:
            return '0'

    # cine incepe
    @staticmethod
    def primul_jucator():
        if random.randint(0, 1) == 0:
            return 'calculator'
        else:
            return 'utilizator'

    def initializare_jucatori(self):
        primul = self.primul_jucator()
        start = self.inceput()
        for i in self.jucatori.keys():
            if i == primul:
                self.jucatori[i] = start
        urmator = 'X'
        if start == 'X':
            urmator = '0'
        for i in self.jucatori.keys():
            if self.jucatori[i] == '_':
                self.jucatori[i] = urmator
        return primul
    # def cine_joaca(self):
    #     rand = joc.initializare_jucatori()


    def alegecalculator(self):
        self.verific = True
        while self.verific:
            alege = random.randint(0, 9)
            if int(alege) in (0, 9):
                for key, value in self.dictionar:
                    if key == int(alege):
                        poz = value
                        if self.tablaDeJoc[int(poz[0])][int(poz[1])] == '_':
                            self.tablaDeJoc[int(poz[0])][int(poz[1])] = self.jucatori[self.muta]
                            self.mutari += 1
                            self.muta = 'utilizator'
                            self.verific = False
                            print(self.tablaDeJoc[0], f"\n{self.tablaDeJoc[1]}", f'\n{self.tablaDeJoc[2]}')

    def alege_utilizator(self):
        self.verific = True
        while self.verific:
            alege = input('Selecteaza unde vrei sa pui ' + self.jucatori[self.muta] + ': ')
            if int(alege) in (0, 9):
                for key, value in self.dictionar:
                    if key == int(alege):
                        poz = value
                        if self.tablaDeJoc[int(poz[0])][int(poz[1])] == '_':
                            self.tablaDeJoc[int(poz[0])][int(poz[1])] = self.jucatori[self.muta]
                            self.mutari += 1
                            self.muta = 'calculator'
                            self.verific = False
                            print(self.tablaDeJoc[0], f"\n{self.tablaDeJoc[1]}", f'\n{self.tablaDeJoc[2]}')
                        else:
                            print('Pozitia selectata este deja ocupata, alegeti altceva')
            else:
                print("Alege o alta pozitie, cea selectata anterior nu se gaseste pe tabla de joc")
                print(self.tablaDeJoc[0], f"\n{self.tablaDeJoc[1]}", f'\n{self.tablaDeJoc[2]}')

    def castigator(self):
        raspuns = 'again'
        for i in range(0, 3):
            if 'X' in self.tablaDeJoc[i] and '0' not in self.tablaDeJoc[i] and '_' not in self.tablaDeJoc[i]:
                print('A castigat "X"')
                raspuns = input('Tastati daca vreti sa continuati ')
                return raspuns
            elif '0' in self.tablaDeJoc[i] and 'X' not in self.tablaDeJoc[i] and '_' not in self.tablaDeJoc[i]:
                print('A castigat "0"')
                raspuns = input('Tastati daca vreti sa continuati ')
                return raspuns
        for i in range(0, 3):
            if self.tablaDeJoc[0][i] == 'X' and self.tablaDeJoc[1][i] == 'X' and self.tablaDeJoc[2][i] == 'X':
                print('A castigat "X"')
                raspuns = input('Tastati daca vreti sa continuati ')
                return raspuns
            elif self.tablaDeJoc[0][i] == '0' and self.tablaDeJoc[1][i] == '0' and self.tablaDeJoc[2][i] == '0':
                print('A castigat "0"')
                raspuns = input('Tastati daca vreti sa continuati ')
                return raspuns
        if self.tablaDeJoc[0][0] == 'X' and self.tablaDeJoc[1][1] == 'X' and self.tablaDeJoc[2][2] == 'X':
            print('A castigat "X"')
            raspuns = input('Tastati daca vreti sa continuati ')
            return raspuns
        elif self.tablaDeJoc[0][0] == '0' and self.tablaDeJoc[1][1] == '0' and self.tablaDeJoc[2][2] == '0':
            print('A castigat "0"')
            raspuns = input('Tastati daca vreti sa continuati ')
            return raspuns
        elif self.tablaDeJoc[0][2] == 'X' and self.tablaDeJoc[1][1] == 'X' and self.tablaDeJoc[2][0] == 'X':
            print('A castigat "X"')
            raspuns = input('Tastati daca vreti sa continuati ')
            return raspuns
        elif self.tablaDeJoc[0][2] == '0' and self.tablaDeJoc[1][1] == '0' and self.tablaDeJoc[2][0] == '0':
            print('A castigat "0"')
            raspuns = input('Tastati daca vreti sa continuati ')
            return raspuns
        return raspuns

    def egalitate(self):
        print('Este egalitate')
        print(self.tablaDeJoc[0], f"\n{self.tablaDeJoc[1]}", f'\n{self.tablaDeJoc[2]}')
        return input('Tastati daca vreti sa continuati ')


def main():
    continua = "Da"
    while continua.upper() == "DA":
        mutari = 0
        joc = Tabla()
        rand = joc.initializare_jucatori()
        while mutari < 9:
            verific = True
            while verific:
                muta = rand
                if rand == 'calculator':
                    muta, mutari, verific = joc.alegecalculator(muta, mutari, verific)
                else:
                    muta, mutari, verific = joc.alege_utilizator(muta, mutari, verific)
                rand = muta
            iesire = 'again'
            if mutari > 4:
                iesire = joc.castigator()
            if iesire != 'again':
                continua = iesire
                break
            if mutari == 9 and iesire == 'again':
                continua = joc.egalitate()

main()
