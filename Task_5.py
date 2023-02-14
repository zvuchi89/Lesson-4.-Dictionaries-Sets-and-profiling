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


