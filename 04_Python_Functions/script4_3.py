"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
"""


def string_to_dict(lst):
    res = {}
    start = int(lst.split()[0])
    stop = int(lst.split()[1])

    if start > stop:
        tmp = start
        start = stop
        stop = tmp

    for i in range(start, stop + 1):
        res[chr(i)] = i

    return res


txt = input('введите два числа через пробел: ')
txt = '800 48'
print(string_to_dict(txt))
