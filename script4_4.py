"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
"""

def sort_data(data):
    for i in range(len(data) - 1):
        index = i
        for j in range(i+1, len(data)):
            if data[j] < data[index]:
                index = j
        if index != i:
            data[index], data[i] = data[i], data[index]


data = [3, 2, 9, 6, 5, 1, 7, 4, 8]
print(data)
sort_data(data)
print(data)