"""
Задание №2
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

data = "abracadabra"
dct = {el: ord(el) for el in data}
print(dct)
