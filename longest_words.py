# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file),
# которая записывает в файл result.txt слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r', encoding='utf-8') as same_file:
        list_lines = same_file.read().splitlines()
        list_words_split = [x.split(' ') for x in list_lines]
        list_words = []
        for i in list_words_split:
            for j in range(len(i)):
                list_words.append(i[j])
        word_max_len = ''
        for i in list_words:
            if len(i) > len(word_max_len):
                word_max_len = i
        list_word_max_len = [x for x in list_words if len(x) == len(word_max_len)]
        with open('result.txt', 'w', encoding='utf-8') as res:
            for el in list_word_max_len:
                res.write(str(el) + '\n')


longest_words('article.txt')
