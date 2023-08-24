def print_innstructins():
    return print('Выберите действие: \n 1 - Записать данные в файл \n 2 - Печать всех данных \n 3 - Поиск по Фамилии \n 4 - Удаление контакта \n 5 - Изменить контакт\n -1 - Завешить')



def write(text):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.writelines(text)
        f.writelines("\n")
        print("Успешно")

def read_all():
    # if "data.txt".exists():
    with open("data.txt", "r", encoding="utf-8") as f:
        # f.readlines()
        for line in f:
            print(line[:-1])

def get_by_name(name):
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            if name in line:
                print(line)
        

def choose(choice):
    if choice == '1': return write(input("Введите ваши данные пример:(фамилия имя отчество номер телефона): "))
    if choice == "2": return read_all()
    if choice == "3": return get_by_name(input("Введите имя или фамилию: "))
    if choice == "4": return delete_contact()
    if choice == "5": return replace_line()
    if choice == "-1": exit()

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def delete_contact():
    with open("data.txt", "a", encoding="utf-8") as f:
        lines = 1
        file = open("data.txt")
        for line in file:
            print (lines, line[:-1])
            lines += 1
        fn = 'data.txt'
        f = open(fn)
        output = []
        fam = input('Введите фамилию для удаления контакта из списка или нажмите enter для удаления всего списка: ')
        for line in f:
            if not fam in line:
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()

def replace_line():
    with open("data.txt", "a", encoding="utf-8") as f:
        lines = 1
        file = open("data.txt")
        for line in file:
            print (lines, line[:-1])
            lines += 1
    id = int(input('Введите id номер контакта для изменения: '))
    lines -= 1
    if lines >= id:
        id -= 1
        text = input('Введите изменения контакта: ')
        lines = open('data.txt', 'r').readlines()
        lines[id] = text + '\n'
        out = open('data.txt', 'w')
        out.writelines(lines)
        # replace_line('data.txt', 0, text)
        out.close()
    else:
        print('Контакта с таким id нет в справочнике!!!')

'''
ere trr yty 2334
fdf ee ttry 3443
sdw rer hgfbt 5554
dsse fgfg hght 5454
'''