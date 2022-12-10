from bs4 import BeautifulSoup
import pandas as pd

# tables2 = pd.read_html('https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BD%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F_COVID-19', match='стран')
url = 'https://ru.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81%D1%82%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C'
tables = pd.read_html(url)
# tables.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
df = tables[0]
abc_tables = df[df.columns[[0, 1, 2]]]

headers = abc_tables.columns.values.tolist()
abc_tables = abc_tables.values.tolist()
# abc_tables.insert(0, headers)


def abc():
    return abc_tables

#Функция поиска частотности получаемой буквы
def find_letter(letter):
    for i in abc_tables:
        if letter == i[0][0]:
            return i[2]


