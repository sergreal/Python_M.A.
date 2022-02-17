
# ******************** 1 ********************

from sys import argv
def salary():
    try:
        script_name, name, time, rate, bonus = argv
        print('Имя скрипта: ', script_name)
        print('Сотрудник: ', name)
        print('Отработано часов: ', time)
        print('Ставка в час: ', rate)
        print('Премия: ', bonus)
        print(f'К выдаче: {int(time) * int(rate) + int(bonus)}')
    except ValueError:
        print('Введите через пробел: фамилию сотрудника, отработанные часы, ставка в час, сумма премии')

salary()


# v terminal  -   python salary_calc.py Ivanov 168 1000 10000
# Имя скрипта:  salary_calc.py
# Сотрудник:  Ivanov
# Отработано часов:  168
# Ставка в час:  1000
# Премия:  10000
# К выдаче: 178000

# ******************** 2 ********************

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(result_list)

# ******************** 3 ********************

my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# ******************** 4 ********************

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [el for el in my_list if my_list.count(el) == 1]
print(result_list)

# ******************** 5 ********************

from functools import reduce

my_list = [el for el in range(100, 1001, 2)]
print('Список чётных чисел от 100 до 1000: ', my_list)

def func_1(el_1, el_2):
    return el_1 * el_2

print(f'Произведение данных чисел: {reduce(func_1, my_list)}')

# ******************** 6 ********************

from itertools import cycle

c = 1
for num in cycle([1, 2, 3, 4, 5]):
    print(num)
    if c >= 10:
        break
    c += 1

# ******************** 7 ********************

def fact(number):
    num = 1
    for n in range(number + 1):
        yield f'{n}! = {num}'
        num *= n + 1

for el in fact(int(input('Факториал числа: '))):
    print(el)
