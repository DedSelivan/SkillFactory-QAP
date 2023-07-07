# У вас есть заготовка функции — def get_wind_class(speed). 
# Вам нужно вместо ??? написать код, который возвращает из функции класс ветра в зависимости от его характера:

# от 1 до 4 м/с включительно - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"

def get_wind_class(speed):
    if  0 < speed < 5:
        return 'weak [1]'
    elif 4 < speed < 11:
        return 'moderate [2]'
    elif 10 < speed < 19:
        return 'strong [3]'
    else:
        return 'hurricane [4]'


print(get_wind_class(speed=int(input("Введите характер ветра: "))))