from import_words import wordlist


print("Добро пожаловать в подбор слов для игры 5 букв! \nДля начала вот 10 слов с самыми распространенными буквами \n")
print(wordlist()[:10])
history = [[], []]
while True:
    # Вводим слово и цвета
    word = input('Введите слово \n').lower()

    while len(word) != 5:
        print('Слово некорректно')
        word = input('Введите слово \n').lower()

    color_of_word = input('Введите полученные цвета без пробелов (Б,С,Ж) \n').lower()

    while len(color_of_word) != 5:
        print('Слово некорректно')
        color_of_word = input('Введите полученные цвета без пробелов (Б,С,Ж) \n').lower()


    history[0].append(word)
    history[1].append(color_of_word)

    # исключаем из списка слова не совпадающие с желтыми буквами
    exceptions_for_yellow = [[], []]
    clear_wordlist = []
    for i in range(len(history[1])):
        for h in range(len(history[1][i])):
            if history[1][i][h] == 'ж':
                exceptions_for_yellow[0].append(history[0][i][h])
                exceptions_for_yellow[1].append(h)
    for i in range(len(wordlist())):
        word_from_wordlist = wordlist()[i]
        yellow_letters = exceptions_for_yellow[0]
        wordlist_letters = []
        for j in exceptions_for_yellow[1]:
            wordlist_letters.append(word_from_wordlist[j])
        if wordlist_letters == yellow_letters:
            clear_wordlist.append(word_from_wordlist)

    # создаем список серых букв для исключения
    gray_letter_list = []
    for i in range(len(history[1])):
        for h in range(len(history[1][i])):
            if history[1][i][h] == 'с':
                gray_letter_list.append(history[0][i][h])

    # исключаем слова содержащие серые буквы
    for i in range(len(clear_wordlist)):
        for j in range(len(gray_letter_list)):
            if gray_letter_list[j] in clear_wordlist[i]:
                clear_wordlist[i] = '_'
    for i in range(clear_wordlist.count('_')):
        clear_wordlist.remove('_')

    # фильтруем слова с учетом белых букв
    exceptions_for_white = [[], []]

    for i in range(len(history[1])):
        for h in range(len(history[1][i])):
            if history[1][i][h] == 'б':
                exceptions_for_white[0].append(history[0][i][h])
                exceptions_for_white[1].append(history[1][i][h])

    for i in range(len(clear_wordlist)):
        tmp_clear_wordlist = list(clear_wordlist[i]), [_ for _ in range(len(clear_wordlist[i]))]
        tmp_count_white_word = 0
        for j in range(len(clear_wordlist[i])):
            for g in range(len(exceptions_for_white[0])):
                if tmp_clear_wordlist[0][j] == exceptions_for_white[0][g] \
                        and tmp_clear_wordlist[1][j] == exceptions_for_white[1][g]:
                    clear_wordlist[i] = '_'
                if exceptions_for_white[0][g] in clear_wordlist[i]:
                    tmp_count_white_word += 1
            if tmp_count_white_word < len(exceptions_for_white[0]):
                clear_wordlist[i] = '_'

    for i in range(clear_wordlist.count('_')):
        clear_wordlist.remove('_')

    print(clear_wordlist[0:10])
    print('осталось подходящих вариантов:', len(clear_wordlist))

    if input('продолжим? да/нет \n').lower() == 'нет':
        break
print('До новых встреч!')