"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
n = float(input('Enter any number:'))
print(f'Result is {n + n*11+ n*111}')
