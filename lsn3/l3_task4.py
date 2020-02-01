"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

"""


def my_pow(x, y):
    res = x
    y = -1 * y
    for i in range(y - 1):
        res = res * x
        i += 1
    return 1 / res


while True:
    x = float(input('Enter x:'))
    y = int(input('Enter y with "-" sigh:'))

    if y < 0:
        result = my_pow(x, y)
        print(f'Result is {result}, cheking by ** is {x ** y}')
    else:
        print('"y" should be less Zero.')
