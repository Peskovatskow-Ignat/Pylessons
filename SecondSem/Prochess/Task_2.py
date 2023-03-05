"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""
from multiprocessing import Process

file_name = "New.txt"


def write():
    global file_name
    d = 4
    sh = 4
    v = 4
    itog = (d * v * 2) + (sh * v * 2)
    with open(f"{file_name}", "w+") as f:
        f.write(str(itog) + "\n")
        pass


def read():
    global file_name
    with open(f"{file_name}", "r") as f:
        x = f.read()
    with open(f"{file_name}", "a+") as file:
        file.write(f"Количество краски чтобы покрасить данное помещение {int(x) * 5}")


if __name__ == "__main__":
    p1 = Process(target=write)
    p2 = Process(target=read)
    p1.start()
    p1.join()
    p2.start()
