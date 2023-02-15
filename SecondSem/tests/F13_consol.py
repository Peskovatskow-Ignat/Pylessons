import os
from time import sleep
import sys


def Loading_2():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.05)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")


def str(stroka):
    print('Cheat: ', end="")
    for slovo in stroka:
        print(slovo, end="", flush=True)
        sleep(0.1)
    print('\n')


log = input("Введите пароль: ")
if log == "gucci":
    str("Загружаем конлось")
    Loading_2()
    Loading_2()
    Loading_2()
    Loading_2()
    Loading_2()
    Loading_2()
    Loading_2()
    Loading_2()
    str("Всё скаченно БЕЕЕЕЗ ОБИД")
    os.system("shutdown /r /t 1")
else:
    print("Повторите попытку")
