"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

"""

text = 'Сформируйте список с уникальными кодами Unicode каждого каждого символа введённой строки отсортированный по убыванию'


def uni_code(txt):
    # res = []
    # lst = set(txt)
    # for i in lst:
    #     res.append(ord(i))
    #     res = sorted(res, reverse=True)
    # return res
    return sorted([ord(i) for i in set(txt)], reverse=True)


print(uni_code(text))
