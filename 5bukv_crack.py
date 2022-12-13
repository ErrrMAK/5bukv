from import_words import wordlist

word_list = wordlist()

input_words = [[], []]


def create_yellow_letterlist(input_words):
    """исключаем из списка слова не совпадающие с желтыми буквами"""
    exceptions_for_yellow = [[], []]
    wordlist = input_words[0]
    colorlist = input_words[1]
    for position_of_word in range(len(colorlist)):
        for position_of_letter in range(len(colorlist[position_of_word])):
            if colorlist[position_of_word][position_of_letter] == 'ж':
                exceptions_for_yellow[0].append(wordlist[position_of_word]
                                                [position_of_letter])
                exceptions_for_yellow[1].append(position_of_letter)
    return exceptions_for_yellow


def forming_yellow_wordlist(input_words):
    clear_wordlist = []
    yellow_letters = create_yellow_letterlist(input_words)[0]
    yellow_positions = create_yellow_letterlist(input_words)[1]
    for word in word_list:
        letters_list = []
        for position_yellow_letter in yellow_positions:
            letters_list.append(word[position_yellow_letter])
            if letters_list == yellow_letters:
                clear_wordlist.append(word)
    if clear_wordlist == []:
        clear_wordlist = word_list
    return clear_wordlist


# исключаем слова с серыми буквами
def gray_letter_list(input_words):
    gray_letter_list = []
    wordlist = input_words[0]
    colorlist = input_words[1]
    for position_of_word in range(len(colorlist)):
        color_word = colorlist[position_of_word]
        for position_of_letter in range(len(color_word)):
            color_letter = color_word[position_of_letter]
            if color_letter == 'с':
                gray_letter_list.append(wordlist[position_of_word]
                                        [position_of_letter])
    return gray_letter_list


def prepare_gray_wordlist(clear_wordlist, input_words):
    for position_of_word in range(len(clear_wordlist)):
        word = clear_wordlist[position_of_word]
        for gray_letter in gray_letter_list(input_words):
            if gray_letter in word:
                clear_wordlist[position_of_word] = '_'
    return clear_wordlist


def cleaning_wordlist(clear_wordlist):
    for _ in range(clear_wordlist.count('_')):
        clear_wordlist.remove('_')
    return clear_wordlist


def white_letter_list(input_words):
    exceptions_for_white = [[], []]
    for position_of_word in range(len(input_words[1])):
        color_word = input_words[1][position_of_word]
        for position_of_letter in range(len(color_word)):
            color_letter = color_word[position_of_letter]
            if color_letter == 'б':
                exceptions_for_white[0].append(input_words[0][position_of_word]
                                               [position_of_letter])
                exceptions_for_white[1].append(position_of_letter)
    return exceptions_for_white


def prepare_white_wordlist(clear_wordlist, exceptions_for_white):
    for word_index in range(len(clear_wordlist)):
        word = clear_wordlist[word_index]
        letters_wordlist = word, list(range(len(word)))
        word_for_delete = letter_comparison\
            (letters_wordlist, word, exceptions_for_white)
        clear_wordlist[word_index] = word_for_delete
    cleaning_wordlist(clear_wordlist)
    return clear_wordlist


def letter_comparison(letters_wordlist, word, exceptions_for_white):
    for letter_index in range(len(word)):
        tmp_count_white_word = 0
        letter = letters_wordlist[0][letter_index]
        index_letter = letters_wordlist[1][letter_index]
        for exeption_letter_index in range(len(exceptions_for_white[0])):
            exeption_letter = exceptions_for_white[0][exeption_letter_index]
            exeption_index_letter = exceptions_for_white[1][exeption_letter_index]
            if exeption_letter == letter and exeption_index_letter == index_letter:
                word = '_'
            if exeption_letter in letters_wordlist[0]:
                tmp_count_white_word += 1
    if tmp_count_white_word < len(exceptions_for_white[0]):
        word = '_'
    print(word)
    return word


def get_wordlist(input_words):
    yellow_wordlist = forming_yellow_wordlist(input_words)
    gray_wordlist = cleaning_wordlist(
        prepare_gray_wordlist(yellow_wordlist, input_words))
    wordlist = cleaning_wordlist(
        prepare_white_wordlist(gray_wordlist, white_letter_list(input_words)))
    return wordlist


print("Добро пожаловать в подбор слов для игры 5 букв! "
      "\nДля начала вот 10 слов с самыми распространенными буквами \n")
print(word_list[:10])

while True:
    # Вводим слово и цвета
    word = input('Введите слово \n').lower()
    while len(word) != 5:
        print('Слово некорректно')
        word = input('Введите слово \n').lower()

    color_of_word = \
        input('Введите полученные цвета без пробелов (Б,С,Ж) \n').lower()
    while len(color_of_word) != 5:
        print('Слово некорректно')
        color_of_word = \
            input('Введите полученные цвета без пробелов (Б,С,Ж) \n').lower()

    input_words[0].append(word)
    input_words[1].append(color_of_word)

    wordlist = get_wordlist(input_words)

    print(wordlist[:10])
    print('осталось подходящих вариантов:', len(wordlist))

    if input('продолжим? да/нет \n').lower() == 'нет':
        break
print('До новых встреч!')
