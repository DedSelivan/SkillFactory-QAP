# Напишите программу, которая на вход принимает текст и выводит количество уникальных символов.

myText = list(set(input('Введите текст: ')))
print(f'Количество уникальных символов: {len(myText)}')
