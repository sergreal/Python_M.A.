# Lesson_3


# ex.1
# def my_calc(num1, num2):
#     return num1 / num2 if num2 !=0 else 'Делить на 0 нельзя.'
# num1 = int(input('Введите число А: '))
# num2 = int(input('Введите число В: '))
#
# print(my_calc(num1, num2))


# ex.2
# def person(name=0, surename=0, year=0, city=0, email=0, phone=0):
#     print(surename, name, year, city, phone, email)
#
# person(
#     name='Серж',
#     surename='Настойчивый_и_Упертый',
#     year='1979г.р.',
#     city='г.Москва',
#     email='strogalev.s@gmail.com',
#     phone='+7(903)114-**-**'
# )


# ex.3
# def my_func(num1, num2, num3):
#
#     if num1 >= num3 and num2 >= num3:
#         return num1 + num2
#     elif num1 >= num2 and num3 >= num2:
#         return num1 + num3
#     else:
#         return num2 + num3
#
# print(f'Сумма двух максимальных чисел: {my_func(num1=int(input("Введите первое число: ")), num2=int(input("Введите второе число: ")), num3=int(input("Введите третье число: ")))}')


# ex.4
# def my_func(x, y):
#     return x**y
# x = int(input('Введите положительное число x: '))
# y = int(input('Введите отрицательное число y: '))
# print(my_func(x, y))


# ex.6
# def int_func():
#     word = input('Введите слово с маленькой буквы: ')
#     return word.title()
# print(int_func())
