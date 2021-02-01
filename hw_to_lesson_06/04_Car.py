# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed = 0
    color = "color"
    name = "name"
    is_police = False

    def go(self, speed):
        self.speed = speed
        print(f"Установлена скорость {self.speed} км/ч")

    def stop(self):
        self.speed = 0
        print(f"Установлена скорость {self.speed} км/ч")

    def turn(self, direction):
        print(f"Совершен разворот {direction} на скорости {self.speed}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed} км/ч")

    def __init__(self, name, color):
        self.name = name
        self.color = color


class TownCar(Car):
    myName = __qualname__

    def show_speed(self):
        max_speed = 60
        print(f"Текущая скорость {self.speed} км/ч")
        if self.speed > max_speed:
            print(f"Внимание! Превышение предельной скорости для {self.myName} - {max_speed} км/ч")


class SportCar(Car):
    myName = __qualname__


class WorkCar(Car):
    myName = __qualname__

    def show_speed(self):
        max_speed = 40
        print(f"Текущая скорость {self.speed} км/ч")
        if self.speed > max_speed:
            print(f"Внимание! Превышение предельной скорости для {self.myName} - {max_speed} км/ч")


class PoliceCar(Car):
    myName = __qualname__
    is_police = True



car_1 = PoliceCar('BMW, 720', 'Black')
print(f"{car_1.color = }")
print(f"{car_1.is_police = }")
print('-----------------')
car_2 = TownCar('Toyota Camry', "Orange")
print(f"{car_2.speed = }")
car_2.speed = 100
print(f"{car_2.speed = }")
car_2.show_speed()
print('-----------------')
car_3 = SportCar('Ferrari', 'Red')
car_3.show_speed()
car_3.go(100)
car_3.turn('направо')
print(f"{car_3.is_police = }")