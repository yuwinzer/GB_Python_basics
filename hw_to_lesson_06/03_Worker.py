# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, income=0):
        self.name = name
        self.surname = surname
        self.position = position
        sal_dict = {"wage": income, "bonus": round(income * 0.1)}
        self._income = sal_dict


class Position(Worker):

    def get_full_name(self):
        get_full_name = f"Full name is {self.name} {self.surname}"
        print(get_full_name)

    def get_total_income(self):
        get_total_income = f"Total income is {self._income['wage'] + self._income['bonus']}"
        print(get_total_income)


worker_1 = Position("John", "Smith", "Engineer", 50000)

print("Атрибуты:")
print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
print(worker_1._income)

print("\nМетоды:")
worker_1.get_full_name()
worker_1.get_total_income()
