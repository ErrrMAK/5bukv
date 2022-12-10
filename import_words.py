import requests
import pandas as pd
from bs4 import BeautifulSoup
from ABC import frequensy_by_letter


def wordlist():
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
    for word in done_words:
        base_frequency.append(frequency_word(word))

    base = {
        'word': done_words,
        'id': base_frequency,
    }


    # Сортируем базу
    base = pd.DataFrame(base).sort_values(by='id', ascending=False)
    base = list(base.set_index('id')['word'])
    return base


def frequency_word(word):
    frequency = 0
    tmp_word = ''
    for letter in word:
        if tmp_word.find(letter) == -1:
            frequency += frequensy_by_letter(letter)
        tmp_word += letter
    return frequency

