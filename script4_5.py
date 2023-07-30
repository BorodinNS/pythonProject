"""
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
  имена str,
  ставка int,
  премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""

names = ['Борис', 'Иван', 'Петр', "Сергей"]
salaries = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85%']


def calc_bonus(name, salary, award):
    # res = {}
    # for name, salary, award in zip(names, salaries, awards):
    #     bonus = salary * float(award[:-1]) / 100
    #     res[name] = bonus
    # return res

    return {name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)}

result = calc_bonus(names, salaries, awards)
print(result)
