lista = ['palarie', 'restaurant', 'apartament', 'parametru', 'mere']


class Spanzuratoarea:
    def __init__(self, cuvant_ales):
        self.cuvant_ales = cuvant_ales
        self.cuvant_format = list(self.cuvant_ales)
        self.litere_verificate = ''
        self.incercari = 0

    def desenare_spanzuratoare(self):
        stadiu = ["""
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
        return stadiu[self.incercari]

    def printare(self):
        print(f'{self.cuvant_format} \n Mai aveti {7 - self.incercari} incercari')
        print(self.desenare_spanzuratoare())

    def initializare_cuvant_format(self):
        lungime = len(self.cuvant_ales)
        for i in range(1, lungime-1):
            if self.cuvant_ales[i] != self.cuvant_ales[0] and self.cuvant_ales[i] != self.cuvant_ales[lungime-1]:
                self.cuvant_format[i] = '_'
        self.litere_verificate = self.cuvant_ales[0]+self.cuvant_ales[lungime-1]

    def verificare_litera(self):
        self.printare()
        litera = input('Introduceti o litera pe care doriti sa o verificati:')

        if litera.isalpha():
            if litera in self.litere_verificate:
                print('Litera a fost deja incercata, alegeti altceva')
            else:
                if litera in self.cuvant_ales:
                    for i in range(len(self.cuvant_ales)):
                        if self.cuvant_ales[i] == litera:
                            self.cuvant_format[i] = litera
                            self.litere_verificate += litera
                else:
                    self.litere_verificate += litera
                    self.incercari += 1
                    print('Litera nu se regaseste in cuvant')

    def verificare_cuvant(self):
        if self.cuvant_format == list(self.cuvant_ales):
            print('Ati castigat, jocul s-a terminat!!')
            return False
        elif self.incercari == 7:
            print('Ati pierdut, nu mai aveti nicio incercare')
            return False
        else:
            return True

    def joc(self):
        self.initializare_cuvant_format()
        while True:
            self.verificare_litera()
            if not self.verificare_cuvant():
                return True


continua = 'Y'
while continua == 'Y':
    a = int(input('Alegeti pozitia unui cuvant din lista: '))
    jocnou = Spanzuratoarea(lista[a])
    ok = jocnou.joc()
    if ok:
        continua = input('Doriti sa reincepeti un joc nou? Y/N ')

