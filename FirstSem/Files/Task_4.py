# """
# Разработайте программу, которая будет показывать слово (или слова),
# чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать). Сначала пользователь
# должен ввести имя файла для обработки. После этого вы должны открыть
# файл и  проанализировать его построчно, разделив при этом строки по
# словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры
# """
#
# Froz = {}
# with open('Slodf.txt', 'r+') as file_1:
#     for line in file_1.readlines():
#         for sym in line.lower().split():
#             for rep in sym:
#                 if rep in ',/.-!@#$%^&+)(*&}{][':
#                     sym = sym.replace(rep, '')
#             Froz[sym] = 0
#     file_1.seek(0)
#     for line_2 in file_1.readlines():
#         for sym in line_2.lower().split():
#             for rep in sym:
#                 if rep in ',/.-!@#$%^&+)(*&}{][':
#                     sym = sym.replace(rep, '')
#             Froz[sym] += 1
#
# Froz = sorted(Froz, key=lambda x: Froz[x])
#
# print(Froz[0])

import time

def Predlog(stroka):
    print("vita: ", end="")
    for slovo in stroka:
        print(slovo, end="", flush=True)
        time.sleep(0.1)
    print('\n')

Predlog('654321tyfguhijioucfgcgvhbjkn')
























# text = '''
# Существует культ Питона, называемый "Дзеном Питона" (The Zen of Python).
# Автором этих постулатов считается Тим Пейтерс.
# Основные постулаты:
# Красивое лучше, чем уродливое.
# Явное лучше, чем неявное.
# Простое лучше, чем сложное.
# Сложное лучше, чем запутанное.
# Плоское лучше, чем вложенное.
# Разреженное лучше, чем плотное.
# Читаемость имеет значение.
# Особые случаи не настолько особые, чтобы нарушать правила.
# При этом практичность важнее безупречности.
# Ошибки никогда не должны замалчиваться.
# Если не замалчиваются явно.
# Встретив двусмысленность, отбрось искушение угадать.
# Должен существовать один — и, желательно, только один — очевидный способ сделать это.
# Хотя он поначалу может быть и не очевиден, если вы не голландец. [1]
# Сейчас лучше, чем никогда.
# Хотя никогда зачастую лучше, чем прямо сейчас.
# Если реализацию сложно объяснить — идея плоха.
# Если реализацию легко объяснить — идея, возможно, хороша.
# Пространства имён — отличная штука! Будем делать их побольше.'''
#
# lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')']  # и т.д.
# lst = []
#
# for word in text.lower().split():
#     if not word in lst_no:
#         _word = word
#         if word[-1] in lst_no:
#             _word = _word[:-1]
#         if word[0] in lst_no:
#             _word = _word[1:]
#         lst.append(_word)
#
# _dict = dict()
# for word in lst:
#     _dict[word] = _dict.get(word, 0) + 1
#
# # сортируем словарь посредством формирования списка (значение, ключ)
# _list = []
# for key, value in _dict.items():
#     _list.append((value, key))
#     _list.sort(reverse=True)
#
# # печатаем первые 10 самых используемых слов
# print('Первые 10 самых используемых слов:')
# for freq, word in _list[0:10]:
#     print(f'{word:>10} -> {freq:>3}')
#
# print('\nили так: (с условием, что длина слова > 4- букв) \n')
# _dict = {(i, lst.count(i)) for i in lst}
# _list = []
#
# for word, kol in _dict:
#     _list.append((kol, word))
#     _list.sort(reverse=True)
#
# for freq, word in _list[0:20]:
#     if len(word) > 4:
#         print('{0:10} {1}'.format(word, freq))