# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def data_func(name, surname, b_year, city, email, phone):
    """Возвращает данные в виде строки"""
    print(f'Subject: {surname} {name}, born in {b_year}. '
          f'Place of residence: {city}. Email {email}, tel: {phone}')


(data_func(name="Ivan", surname="Petrov", b_year='1990',
                city='Moscow', email='mail@gmail.com', phone=89896005030))

