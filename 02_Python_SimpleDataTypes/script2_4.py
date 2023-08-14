""" Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой. """

r = int(input('Введите радиус окружности (радиус не превышает 500): '))
d = 2 * 3.14 * r
s = 3.14 * r ** 2
if r > 500:
    print('Радиус не должен превышать 500')
else:
    print(f'Длина окружности: {d:.42f}')
    print(f'Площадь круга: {s:.42f}')