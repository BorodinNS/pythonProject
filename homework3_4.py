# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import random

a = {"палатка": 4, "спальный мешок": 2.5, "перекус": 0.5, "фонарик": 0.4, "вода": 1.5, "велосипед": 35, "аптечка": 0.5}

maximum_load = 8
counter = 0
lst_artibute = []
while counter < maximum_load:
    key, value = random.choice(list(a.items()))
    if key in lst_artibute:
        continue
    if counter + value > maximum_load:
        break
    counter += value
    lst_artibute += (str(key), str(value))

print(lst_artibute, "=", counter)