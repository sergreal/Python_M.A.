
# ******************** 1 ********************

from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()

# ******************** 2 ********************

class Road:
    def __init__(self, _length, _width, _weight, _thickness):
        self._length = _length
        self._width = _width
        self._weight = _weight
        self._thickness = _thickness

    def mass(self):
        return self._length * self._width * self._weight * self._thickness

class Volume(Road):
    def __init__(self, _length, _width, _weight, _thickness):
        super().__init__(_length, _width, _weight, _thickness)

r = Volume(5000, 20, 25, 5)
print(r.mass())

# ******************** 3 ********************

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Ivan', 'Ivanov', 'Programmer', 100000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

# ******************** 4 ********************

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево.'

    def show_speed(self):
        return f'Скорость движения {self.name} {self.speed} км/ч.'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} выше чем положено'
        else:
            return f'Скорость {self.name} разрешена для городского движения'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} была {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} выше чем разрешено.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции.'
        else:
            return f'{self.name} не из полиции.'

ferrari = SportCar(100, 'Red', 'Ferrari', False)
mazda = TownCar(30, 'Blue', 'Mazda', False)
lada = WorkCar(70, 'White', 'Lada', True)
ford = PoliceCar(110, 'Black',  'Ford', True)
print(lada.turn_left())
print(f'Когда {mazda.turn_right()}, тогда {ferrari.stop()}')
print(f'{lada.go()} с превышением. {lada.show_speed()}')
print(f'{lada.name} это {lada.color}')
print(f'{ferrari.name} из полиции? {ferrari.is_police}')
print(f'{lada.name} из полиции? {lada.is_police}')
print(ferrari.show_speed())
print(mazda.show_speed())
print(ford.police())
print(ford.show_speed())

# ******************** 5 ********************

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'

pen = Pen('Ручку')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
