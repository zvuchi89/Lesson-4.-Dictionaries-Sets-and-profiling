# Lesson-4.-Dictionaries-Sets-and-profiling

#Знакомство с языком Python (семинары)
#Урок 4. Словари, множества и профилирование


# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
#
# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!
#
# Process finished with exit code 0
#
# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0
#
# Process finished with exit code 0


x = float(input(f'Введите первое число: '))
y = float(input(f'Введите первое число: '))
def my_func(x, y):
    try:
        return x // y
    except ZeroDivisionError as my_func:
        print('Вы что? Пытаетесь делить на 0?')

print(my_func(x, y))


# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456


name = input('Введите Фамилию и Имя: ')
birthday = int(input('Ваш год рождения полностью:  '))
city = input('Город где вы проживаете: ')
mail = input('email: ')
telephone = int(input('Телефон: '))

result = map(str.lower, [name, birthday, city, mail, telephone])
print((f'\n {name}, {birthday} года рождения, проживает в городе {city},'
       f' email: {mail}:, телефон: {telephone}'))



# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()


print('Используя функцию sort() \n')
args = (
    int(input('Введите первый аргумент: ')),
    int(input('Введите второй аргумент: ')),
    int(input('Введите третий аргумент: ')),
)
print(sorted(args, reverse=True))
args_1 = (sorted(args, reverse=True))


def sum(args_1):
    return args_1[0] + args_1[1]


print(f'Сумма наибольших двух аргументов: {sum(args_1)} \n')


print('Без функции sort() \n')


def my_func(arg_1, arg_2, arg_3):
    print(f' \n Сумма наибольших двух аргументов равна: '
          f'{(arg_1 + arg_2 + arg_3) - min([arg_1, arg_2, arg_3])}')


my_func(
    int(input('Введите первый аргумент: ')),
    int(input('Введите второй аргумент: ')),
    int(input('Введите третий аргумент: ')),
)



# 4. Программа принимает действительное положительное число x
# и целое отрицательное число y. Необходимо выполнить возведение числа x
# в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень!
# ВНИМАНИЕ: использование встроенной функции = задание не принято

x = int(input('Введите положительное число: '))
y = int(input('Введите отрицательное число: '))

def my_func(x, y):
        if y == 0:
            return 1
        elif y == 1:
            return x
        elif y < 0:
            return 1 / my_func(x, -y)
        return x * my_func(x, y - 1)
print(x * my_func(x, y - 1))




# 5. Сделайте профилирование кода любого или любых выполненных заданий
# с помощью модуля timeit, опишите результат


import timeit

x = int(input('Введите положительное число: '))
y = int(input('Введите отрицательное число: '))

code_to_test = """
def my_func(x, y):
        if y == 0:
            return 1
        elif y == 1:
            return x
        elif y < 0:
            return 1 / my_func(x, -y)
        return x * my_func(x, y - 1)
        
"""

elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)

code_to_test = """
def my_func( x, y):
    print(x**y)
"""
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)

# Чтобы получить точное время, timeit() выполнит 100 циклов. Поэтому вывод
# делим на 100, чтобы получить время выполнения только для одного цикла.
# Результат первого кода = 2.870004391297698e-07 (время выполнения в секундах).
# Считаю, 3 секунды это много для выполнения данной операции.Результат второго
# кода составил на 1 секунду меньше = 1.8700025975704192e-07

#Хотела провести тест и на встроенную функцию pow, но неполучилось. А почему?
#print(pow(x, y))
