"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
Slovar = {'Ivan': 'Golovin', 'Oleg': 'Bobchonok', 'Aleksandr': 'Kylakov', 'Dmitriй': 'Torshin', 'Albert': 'Tenigin'}
del Slovar['Oleg']
Slovar['Ivan'] = 'Tenigin'
Slovar['Albert'] = 'Golovin'
Slovar['new_key'] = 'new_value'
print(Slovar)