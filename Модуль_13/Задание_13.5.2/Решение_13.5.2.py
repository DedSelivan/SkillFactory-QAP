# Задание 13.5.2

x, y = int(input("Введите число x: ")), int(input("Введите число y: "))

if x > 0 and y > 0:
    print("Первая четверть")
if x < 0 and y > 0:
    print("Вторая четверть")
if x < 0 and y < 0:
    print("Третья четверть")
if x > 0 and y < 0:
    print("Четвертая четверть")