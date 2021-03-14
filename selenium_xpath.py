from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
data_values = {'Nr.crt': [], 'Judet': []}
driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')


def link_creat():
    ok = True
    data = None
    while ok:
        data = input('Alegeti data pentru care doriti sa efectuati extragerea: 1-24 pentru luna aprilie ')
        if data in ['5', '13', '22']:
            print('Selectati o alta data')
        else:
            ok = False
    creare_link = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-' + str(data) + '-ianuarie-ora-13-00/'
    a = 'Numar cazuri confirmate la ' + data + '.01'
    return creare_link, a

def extragere_nrcrt_judete():
    nr_crt = []
    for i in range(2, 44):
        k = f'//div/div/table[1]/tbody/tr[{i}]/td[1]'
        get_element = driver.find_element_by_xpath(k)
        nr_crt.append(get_element.text)
    data_values['Nr.crt'] = nr_crt
    judete = []
    for i in range(2, 44):
        k = f'//div/div/table[1]/tbody/tr[{i}]/td[2]'
        get_element = driver.find_element_by_xpath(k)
        judete.append(get_element.text)
    data_values['Judet'] = judete
    return True


def extragere_date():
    date = []
    for i in range(2, 44):
        k = f'//div/div/table[1]/tbody/tr[{i}]/td[3]'
        get_element = driver.find_element_by_xpath(k)
        date.append(get_element.text)
    return date


continua = "Y"
j = 0
while continua == 'Y':
    link, coloana_data = link_creat()
    driver.get(link)
    j += 1
    if j == 1:
        extragere_nrcrt_judete()
    data_values[coloana_data] = extragere_date()
    x = input('Doriti sa extrageti date si pentru alte zile? Y/N')
    if x != 'Y':
        continua = False

lista_coloane = []
for key in data_values:
    lista_coloane.append(key)


df = pd.DataFrame(data_values, columns=lista_coloane)
df.to_excel(r"C:\Users\PC\PycharmProjects\Grupa3SIIT\dateComunicareStrategica.xls", sheet_name='all_datas')


