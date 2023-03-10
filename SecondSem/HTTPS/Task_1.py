"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""
import os
import requests


# os.mkdir("LOVE")
os.chdir(r"LOVE/")
for i in range(1115):
    r = requests.get("https://cataas.com/cat")
    with open(f"Cat{i}.jpg", "wb") as f:
        f.write(r.content)


# def foo_1():
#     for i in range(2):
#         p = requests.get('https://cataas.com/cat')
#         with open(f'cat{i}.jpg', 'wb') as f:
#             f.write(p.content)
#
#
# def foo_2():
#     for i in range(2, 4):
#         p = requests.get('https://cataas.com/cat?type=original')
#         with open(f'cat{i}.jpg', 'wb') as f:
#             f.write(p.content)
#
#
# def foo_3():
#     for i in range(4, 6):
#         p = requests.get('https://cataas.com/cat?filter=pixel')
#         with open(f'cat{i}.jpg', 'wb') as f:
#             f.write(p.content)

#
# foo_1()
# foo_2()
# foo_3()
