"""
Напишите программу которая будет спрашивать пользователя ввод имени пока пользователь не введет off.
Программа должна используя lambda-функцию добавлять к каждому имени надпись "гений".
"""
name_1 = 0
while name_1 != 'off':
    name_1 = input('Введите имя - ')
    mane_2 = lambda name_1: name_1 + ' гений'
    print(mane_2(name_1))