# Задача 38:
#    Дополнить телефонный справочник возможностью изменения и удаления данных.
#    Пользователь также может ввести имя или фамилию, и
#    Вы должны реализовать функционал для изменения и удаления данных


def search_data():
    """
    Эта функция ищет в телефонном справочнике пару ФИО | тел.номер,
    по фамилии, имени, отчеству или телефонному номеру.
    """
    info = input("""Введите один из этих составляющих телефонного справочника:
Фамилия, Имя, Отчесвто, телефонный номер. Обратите внимание, что при вводе ФИО,
будут выводиться все пары ФИО - тел.номер, всех людей имеющий то же ФИО.
""")
    with open('tel_directory.txt', 'r', encoding='utf-8') as file:
        pairs_f_name_tel = file.read().splitlines()
        for i in pairs_f_name_tel:
            if info in i:
                print(i)


def append_data():
    """
    Эта функция позволяет дополнить телефонный справочник
    новой парой ФИО | тел.номер
    """
    print("""Введите данные для добавления в телефонный справочник в формате:
Фамилия Имя Отчество | +7(ххх)-ххх-хххх.
Если хотите ввести несколько пар ФИО | тел.номер, то введите их через enter
Чтобы закончить ввод введите 'end'""")
    flag_append = True
    list_of_input_data = []
    while flag_append:
        input_data = input()
        if input_data == 'end':
            flag_append = False
        else:
            list_of_input_data.append(input_data)
    with open('tel_directory.txt', 'a', encoding='utf-8') as file:
        for i in list_of_input_data:
            file.write(i + '\n')


def show_data():
    """Это функция выводит в консоль всю информацию в телефонном справочнике"""
    with open('tel_directory.txt', 'r', encoding='utf-8') as file:
        list_pair_f_name_tel = file.read().splitlines()
    for i in list_pair_f_name_tel:
        print(i)


def change_and_remove():
    required_data = input(" Введите фамилию, имя, отчество или телефонный\
                         \n номер человека, чтобы удалить или изменить данные о нём\
                         \n : ")
    with open('tel_directory.txt', 'r', encoding='utf-8') as file:
        list_lines = [i.lstrip() for i in file.readlines()]
        for i in list_lines:
            if required_data in i:
                print(i)
    required_data = input("\
     \n Вот похожие данные.\
     \n Теперь напишите данные об искомом человеке полностью в формате:\
     \n Фамилия Имя Отчество | +7(xxx)-xxx-xxxx\
     \n : ")
    print(required_data)
    # маркер - изменить или удалить
    mark = input(" Введите '1' если хотите изменить эти данные\
                \n или '0' если хотите удалить эти данные: ")
    # индекс строки, которая должна быть удалена или изменена
    index_line = 0
    for i in list_lines:
        if required_data in i:
            index_line = list_lines.index(i)

    if mark == '0':
        list_lines.pop(index_line)
    else:
        what_to_change = input("\
            \n Для изменения информации о человеке введите новые\
            \n данные о нём полностью в формате\
            \n Фамилия Имя Отчество | +7(xxx)-xxx-xxxx\
            \n : ")
        list_lines[index_line] = what_to_change
    with open('tel_directory.txt', 'w', encoding='utf-8') as same_file:
        for el in list_lines:
            same_file.write(el)


flag = True
while flag:
    mode = input("Введите\
                \n '1' если хотите найти данные в телефонном справочнике.\
                \n '2' если хотите добавить данные в телефонный справочник.\
                \n '3' показать весь телефонный справочник\
                \n '4' для изменения и удаления данных в телефонном справочнике\
                \n '0' для завершения работы с файлом.\
                \n : ")
    if mode == '1':
        search_data()
    elif mode == '2':
        append_data()
    elif mode == '3':
        show_data()
    elif mode == '4':
        change_and_remove()
    elif mode == '0':
        flag = False
