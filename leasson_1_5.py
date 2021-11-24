#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if proceeds > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {proceeds / costs:.1f}")
    workers = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного сторудника сотавила {proceeds / workers:.1f}")
elif proceeds == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
