"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import os
from time import sleep
from threading import Thread, Lock

flag = False

def bomb():
    global flag
    while True:
        sleep(3)
        if not flag:
            print("\nВводите быстрее: ")
    
th = Thread(target=bomb, daemon=True)
th.start()


kod = input("Введите код бомбы: \n")

if "228" == kod:
    print("Ура бомба обезврежена")
else:
    print("Пока кентик")
    sleep(5)
    os.system("shutdown /r /t 1")

