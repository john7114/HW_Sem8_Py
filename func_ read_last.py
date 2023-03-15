# Напишите функцию read_last(lines, file),
# которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#    Вечерело
#    Жужжали мухи
#    Светил фонарик
#    Кипела вода в чайнике
#    Венера зажглась на небе
#    Деревья шумели
#    Тучи разошлись
#    Листва зеленела

def read_last(lines, file):
    if lines > 0 and type(lines) == int:
        with open(file, 'r', encoding='utf-8') as some_file:
            list_lines = some_file.read().splitlines()
            for i in range(len(list_lines) - lines, len(list_lines)):
                print(list_lines[i])
    else:
        print("Число строк должно быть положительным, целым числом")


quantity_strings = int(input("Введите кол-во строк из файла, которые вы хотите напечатать из конца: "))
read_last(quantity_strings, 'article.txt')
