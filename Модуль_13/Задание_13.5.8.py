# Задание_13.5.8

# Проверьте, все ли элементы в списке являются уникальными.

myList = list(input('Введите символы: '))
myListNew = list(set(myList))

if len(myList) == len(myListNew):
    print('Все элементы списка являются уникальными')
else:
    print('Не все элементы списка уникальны')
