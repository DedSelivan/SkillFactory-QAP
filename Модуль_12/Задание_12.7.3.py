# Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом, 
# что ключ — название банка, значение — процент. 
# Напишите программу, в результате которой будет сформирован список deposit значений — накопленные средства за год вклада 
# в каждом из банков.
# На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.

# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Пример работы программы при

# money = 100000

# deposit = [5600, 5900, 4280, 4000]

# Добавьте в программу поиск максимального значения и его вывод на экран в формате:

# Максимальная сумма, которую вы можете заработать — deposit[i]

# Где вместо deposit[i] будет выведено максимальное значение списка.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input('Введите сумму вклада: '))

deposit = [
    (money * per_cent['ТКБ']) / 100,
    (money * per_cent['СКБ']) / 100,
    (money * per_cent['ВТБ']) / 100,
    (money * per_cent['СБЕР']) / 100
]

print(f'ТКБ:{deposit[0]}, СКБ:{deposit[1]}, ВТБ:{deposit[2]}, СБЕР:{deposit[3]}')
print(f'Максимальная сумма которую можно заработать: {max(deposit)}')


