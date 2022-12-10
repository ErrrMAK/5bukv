from bs4 import BeautifulSoup
import pandas as pd


def pars_wiki():
    url = 'https://ru.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81%D1%82%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C'
    tables = pd.read_html(url)
    df = tables[0]
    abc_tables = df[df.columns[[0, 1, 2]]]
    abc_tables = abc_tables.values.tolist()
    return abc_tables

#глобальная переменная позволяет не ходить каждый раз в Вики
abc_tables = pars_wiki()


# Функция поиска частотности получаемой буквы
def frequensy_by_letter(letter):
    for i in abc_tables:
        if letter == i[0][0]:
            return i[2]