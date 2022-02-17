# ******************** 1 ********************

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 2022:
                    return f'Всё в порядке.'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'

today = Date('8 - 2 - 2022')
print(today)
print(Date.valid(8, 2, 2022))
print(today.valid(11, 13, 2011))
print(Date.valid(42, 11, 2000))

print(Date.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))

# ******************** 2 ********************

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя")

div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(22, 0))
print(DivisionByNull.divide_by_null(33, 0.5))
print(div.divide_by_null(44, 0))

# ******************** 3 ********************

class Check:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Вводите элемент списка, нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение. Вводите только число.")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вводите не числа. Вы вышли'

try_except = Check(1)
print(try_except.my_input())


