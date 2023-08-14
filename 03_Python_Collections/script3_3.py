"""
Задание №3
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""
a = (1, 2.1, 2, 3, True, None, "ghb")
dct = {}
for el_1 in a:
    obj_type = type(el_1)
    lst = []
    for el_2 in a:
        if type(el_2) == obj_type:
            lst.append(el_2)
    dct[obj_type] = lst

print(dct)