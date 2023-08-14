"""
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
        "Петя": ("Палатка", "Котелок", "Топор"),
        "Саша": ("Палатка", "Котелок", "Топор", "Спирт"),
        #"Вика": ("Палатка", "Топор", "Спирт")
        }

lst = []
for k,v in data.items():
    lst.append(set(v))


for i in range(len(lst)-2):
    res_all = lst[i].intersection(lst[i+1])
    res_all = res_all.intersection(lst[i+2])

# print(res_all)

for i in range(len(lst)-1):
    res_unic = lst[i].symmetric_difference(lst[i+1])
    print(res_unic)

print(res_unic)  ## доделать!