
# ******************** 1 ********************

my_file = open("my_file.txt", "w")
while True:
    str_list = input('Enter your Name, Surname. Then press Enter twice. \n- ')
    if not str_list:
        break
    print(str_list, file=my_file)

# ******************** 2 ********************

with open('sc_fik.txt', encoding='utf-8') as file:
    note = [f'{line}. {count.strip()} - {len(count.split())} слов' for line, count in enumerate(file, 1)]
    print(*note, sep='\n')
    print(f'Всего строк - {len(note)}.')

# ******************** 3 ********************

with open('salary.txt', 'r', encoding='utf-8') as file:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in file}
    print(f'Средний доход: ${round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Список сотрудников, с окладом менее $20k: {[el[0] for el in employees_dict.items() if el[1] < 20000]}')

# ******************** 4 ********************

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
with open("dict_1.txt", "w", encoding='utf-8') as dict_1:
    with open("dict_2.txt", encoding='utf-8') as dict_2:
        dict_1.writelines([line.replace(line.split()[0], dictionary.get(line.split()[0])) for line in dict_2])

# ******************** 5 ********************

from random import randint
with open('task_5.txt', mode='w+', encoding='utf-8') as file:
    file.write(' '.join([str(randint(1, 1000)) for _ in range(100000)]))
    file.seek(0)
    print(sum(map(int, file.readline().split())))

# ******************** 6 ********************

my_dict = {}
with open('task_6.txt', encoding='utf-8') as file:
    for line in file:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = name_sum
print(f'{my_dict}')

# ******************** 7 ********************

import json

with open('task_7.json', 'w', encoding='utf-8') as write_f:
    with open('task_7.txt', encoding='utf-8') as file_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in file_obj}
        result = [profit, {'Средняя прибыль': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                    len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)

