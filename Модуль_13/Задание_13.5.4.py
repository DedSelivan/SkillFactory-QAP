# Задание_13.5.4

# Вам дан словарь user_database с именами пользователей и их паролями. 
# Допишите функцию check_user так, чтобы она по логину пользователя проверяла, существует он или нет, 
# после чего с помощью вложенного условия проверяла правильность пароля этого пользователя.


# Функция должна возвращать только True или False.

# Примечание: чтобы вернуть True, напишите "return True"; чтобы вернуть False, напишите "return False".

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(username, password):
    if username in user_database:
        if password in user_database.get(username):
            return True
    else:
        return False

