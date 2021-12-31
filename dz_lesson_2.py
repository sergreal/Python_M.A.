# Lesson_2_ДЗ


# ex.1
#
# spisok = [45, 45.5, 'stroka', True, [3, 4]]
# print(spisok)
# for el in spisok:
#     print(type(el))
#
# print('*'*77)


# ex.2
#
# my_list = list(input('Введите числа от 0 до 9, без пробелов: '))
# for i in range(1, len(my_list), 2):
#     my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
#
# print(my_list)


# ex.3
#
# month_num = int(input('Введите номер месяца: '))
#
# season_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
#         7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
#
# month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
#                  'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#
# if month_num >=1 and month_num <=12:
#    print(f'Время года: {season_dict[month_num]}')
#    print(f'Месяц: {month_list[month_num -1]}')
# else:
#    print('Ошибка.')


# ex.4
#
# var.1
# stroka = input('Напишите скороговорку - "Ехал грека через реку":  ')
# x = stroka.split(' ')
# for i, el in enumerate(x, 1):
#    if len(el) > 10:
#        el = el[0:10]
#    print(f'{i} - {el}')
#
# var.2
# fruits = input('Введите названия разных фруктов, через пробел: ').split()
# for i, word in enumerate(fruits, 1):
#     print(f'{i}. {word[:10]}')


# ex.5
#
# my_list = [9, 8, 7, 6, 4, 3, 1]
# new_number = int(input('Введите новый элемент рейтинга в виде натурального числа: '))
# i = 0
# for n in my_list:
#     if new_number <= n:
#         i += 1
#     else:
#         break
# my_list.insert(i, new_number)
# print(my_list)
