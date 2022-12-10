import requests
import pandas as pd
from bs4 import BeautifulSoup
from ABC import find_letter


# Парсим и подготавливаем базу
url = "http://russkiyslovar.ru/iz-5-bukv"
get = requests.get(url)
soup = BeautifulSoup(get.text, 'lxml')
s = soup.find('div', class_='field-item even').text

base_Words = s.split()
base_Words = base_Words[2:]
done_words = []
base_frequency = []

# Очищаем базу от слов с дефисом
for i in range(len(base_Words)):
    if base_Words[i].find("-") == -1:
        done_words.append(base_Words[i])

# Присваиваем каждому слову ценность (сумма частотностей каждой буквы)
for i in range(len(done_words)):
    tmp_frequency = 0
    tmp_word = ''
    for j in range(len(done_words[i])):
        if tmp_word.find(done_words[i][j]) == -1:
            tmp_frequency += find_letter(done_words[i][j])
        tmp_word += done_words[i][j]
    base_frequency.append(tmp_frequency)

base = {
    'word': done_words,
    'frequency': base_frequency,
    'id': base_frequency,
}

# Сортируем базу
base = pd.DataFrame(base).sort_values(by='id', ascending=False)
base = list(base.set_index('id')['word'])

def wordlist():
    return base
