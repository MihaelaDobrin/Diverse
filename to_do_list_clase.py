import datetime


class Lista:
    def __init__(self):
        self.lista_categorii = []
        self.lista_finala = []
        self.lista_task = []

    def creare_lista_categorii(self):
        while True:
            categorie = input('Introduceti categoria: ')
            if categorie.isalpha() and categorie not in self.lista_categorii:
                self.lista_categorii.append(categorie)
            adauga = input('Doriti sa adaugati o noua categorie? Y/N ')
            if adauga != 'Y':
                return True

    @staticmethod
    def data_si_timp():
        e = 'Error'
        while e != 'ok':
            var_data_time = input("Introduceti Data si Ora dupa formatul: ZZ.LL.AAAA HH:MM:SS  ")
            try:
                datetime.datetime.strptime(var_data_time, '%d.%m.%Y %H:%M:%S')
                e = 'ok'
                return var_data_time
            except ValueError:
                e = 'Error'

    def creare_dictionar(self):
        var_task = input("Alegeti tipul de task: ")
        while True:
            if var_task in self.lista_task:
                var_task = input('Alegeti un task care nu se regaseste deja: ')
            else:
                break
        var_data_time = self.data_si_timp()
        var_responsabil = input("Alegeti un responsabil: ")
        var_categorie = input("Alegeti categoria: ")
        while True:
            if var_categorie not in self.lista_categorii:
                var_categorie = input(f'Alegeti o categorie din lista: {self.lista_categorii} ')
            else:
                break
        var_dictionar = {'task': var_task, 'data': var_data_time, 'persoana': var_responsabil,
                         'categoria': var_categorie}
        self.lista_task.append(var_task)
        return var_dictionar

    def adaugare_in_lista(self):
        while True:
            self.lista_finala.append(self.creare_dictionar())
            utilizator_confirm = input("Vrei sa mai adaugi alte task uri? Y/N ").upper()
            if utilizator_confirm != 'Y':
                break

    def sortare(self, cheie, tip_sortare):
        return sorted(self.lista_finala, key=lambda l: l[cheie], reverse=tip_sortare)

    def alege_tip_sortare(self):
        meniu1 = [self.sortare('task', False), self.sortare('task', True), self.sortare('data', True),
                  self.sortare('data', False), self.sortare('persoana', False), self.sortare('persoana', True),
                  self.sortare('categoria', False), self.sortare('categoria', True)]
        print('''1. sortare ascendentă task
                     2. sortare descendentă task
                     3. sortare ascendentă data
                     4. sortare descendentă data
                     5. sortare ascendentă persoana responsabilă
                     6. sortare descendentă persoană responsabilă
                     7. sortare ascendentă categorie
                     8. sortare descendentă categorie
            ''')
        tip = int(input('Alege un tip de sortare: '))
        if tip in range(1, 9):
            print(meniu1[tip-1])

    def filtrare(self):
        camp = input('Introduceti de la tastatura campul dupa care se realizeaza filtrarea : ')
        caut = input('Introduceti de la tastatura stringul pentru filtrare : ')
        for i in range(len(self.lista_finala)):
            if caut in self.lista_finala[i][camp]:
                return self.lista_finala[i]
        return True

    def editare(self):
        editare = input('Introduceti identificatorul pe care doriti sa-l modificati: "task/persoana/data/categorie"')
        task_modif = input('Introduceti task-ul pe care doriti sa-l modificati: ')
        for i in range(len(self.lista_finala)):
            print(self.lista_finala[i])
            if task_modif == self.lista_finala[i]['task']:
                self.lista_finala[i][editare] = input('Introduceti modificarea pe care doriti sa o realizati: ')
                print('Modificarea a fost realizata')
                return self.lista_finala
        return True

    def stergere_task(self):
        task_sters = input('Introduceti taskul pe care doriti sa-l stergeti: ')
        for i in range(len(self.lista_finala)):
            if self.lista_finala[i]['task'] == task_sters:
                self.lista_task.remove(task_sters)
                self.lista_finala.remove(self.lista_finala[i])
                return self.lista_finala

    def meniu_principal(self):
        print(''' Aceasta este lista de activitati:
                      1. Listare date
                      2. Sortare
                      3. Filtrare
                      4. Adaugare task
                      5. Editare task
                      6. Stergere task
        ''')
        alt = int(input('Selectati activitatea care doriti sa fie realizata: '))
        # lista_activitati = ['', self.sortare('categoria', False), self.alege_tip_sortare(), self.filtrare(),
        #                     self.creare_dictionar(), self.editare(), self.stergere_task()]
        if alt in range(1, 7):
            if alt == 1:
                print(self.sortare('categoria', False))
            if alt == 2:
                self.alege_tip_sortare()
            if alt == 3:
                print(self.filtrare())
            if alt == 4:
                self.lista_finala.append(self.creare_dictionar())
                print(self.lista_finala)
            if alt == 5:
                print(self.editare())
            if alt == 6:
                print(self.stergere_task())
        else:
            print('Nu ati ales o varianta corecta')


joc = Lista()
joc.creare_lista_categorii()
joc.adaugare_in_lista()
while True:
    joc.meniu_principal()
    continuare = input('Doriti sa efectuati o alta activitate? Y/N ')
    if continuare != 'Y':
        break
