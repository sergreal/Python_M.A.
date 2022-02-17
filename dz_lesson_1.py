# DZ_1
#
# name = input('Напишите ваше имя: ')
# print('Доброго времени суток!')
# drink = input(f'Какой ваш любимый напиток, {name}: ')
# year = 2022
#
# print(f'{name}, значит в новогоднюю ночь {year} года, у вас на праздничном столе обязательно будет и {drink}. ))')
#
# salut = input('А вы любите смотреть салют? - ')
# print(f'{name}, обязательно сходите с сеьмей на городскую елку. Обещают красивый салют.')


# DZ_2
#
# number = int(input('Введите любое количество секунд, чтобы перевсти в часы-минуты-секунды: '))
#
# hours = int(number // 3600)
# hours_min = int(number % 3600)
# min = int(hours_min // 60)
# sec = int(hours_min % 60)
#
# print(f'{hours}:{min}:{sec}')
# (можно использовать модули времени)

# DZ_3_var.1
#
# n = int(input('Введите число n: '))
# nn = int(n * 11)
# nnn = int(n * 111)
# print(int(n))
# print(int(nn))
# print(int(nnn))
# print(f'Вы ввели число: {n}. Сумма чисел: {n} + {nn} + {nnn} = {n + nn + nnn}')

# DZ_3_var.2
#
# n1 = input('Введите число n: ')
# n2 = n1 + n1
# n3 = n1 + n1 + n1
# n = int(n1)
# nn = int(n2)
# nnn = int(n3)
# print(int(n))
# print(int(nn))
# print(int(nnn))
# result = n + nn + nnn
# print(f'Считаем:  {n} + {nn} + {nnn} = {result}')


#DZ_4
#
# x = int(input('Введите целое положительное число, от 1тыс., до 1млн..: '))
# max = 0
# while x > 0:
#    c = x % 10
#    if c >= max:
#        max = c
#    x = x // 10
# print('Самая большая цифра в этом числе:', max)


#DZ_5
#
# viruchka = int(input('Введите сумму выручки за прошедший месяц: '))
# rashody = int(input('Введите сумму расходов за прошедший месяц: '))
# if viruchka > rashody:
#     pribyl = int(viruchka - rashody)
#     rentab = round(pribyl / viruchka*100, 2)
#
#     print(f'В прошедшем месяце, прибыль фирмы составляет: {pribyl}')
#     print(f'Рентабельность составляет: {rentab}%')
#
#     sotr = int(input('Введите общее кол-во сотрудников фирмы: '))
#     pribyl_sotr = round(pribyl / sotr, 2)
#     print(f'Прибыль фирмы, в расчете на одного сотрудника, составляет: {pribyl_sotr}')
#
# else:
#     ubitok = int(viruchka - rashody)
#     print(f'В прошедшем месяце, сумма убытка составляет: {ubitok}')


#DZ_6
