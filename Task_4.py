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

