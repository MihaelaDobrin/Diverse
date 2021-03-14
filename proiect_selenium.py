from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')
data_values = {'Nr.crt': [], 'Judet': []}


def extragere_date(k):
    if k == 1:
        nr_crt = []
        for i in range(1, 43):
            nr_crt.append(get_element[i*5].text)
        data_values['Nr.crt'] = nr_crt
        judete = []
        for i in range(1, 43):
            judete.append(get_element[i*5+1].text)
        data_values['Judet'] = judete
    date = []
    for i in range(1, 43):
        date.append(get_element[i*5+2].text)
    return date


def link_creat():
    ok = True
    while ok:
        data = input('Alegeti data pentru care doriti sa efectuati extragerea: 1-24 pentru luna aprilie ')
        if data in ['5', '13', '22']:
            print('Selectati o alta data')
        else:
            ok = False
    creare_link = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-' + data + '-ianuarie-ora-13-00/'
    a = 'Numar cazuri confirmate la ' + data + '.01'
    return creare_link, a


for j in range(1, 6):
    link, coloana_data = link_creat()
    driver.get(link)
    get_element = driver.find_elements_by_tag_name('td')
    data_values[coloana_data] = extragere_date(j)

lista_coloane = []
for key in data_values:
    lista_coloane.append(key)


df = pd.DataFrame(data_values, columns=lista_coloane)
df.to_excel(r"C:\Users\PC\PycharmProjects\Grupa3SIIT\dateComunicare.xls", sheet_name='all_products')
