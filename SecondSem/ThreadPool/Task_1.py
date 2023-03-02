"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
from threading import Thread
from queue import Queue
from time import sleep

queue = Queue()


def kick(queue):
    inp = ''
    sleep(2)
    while inp != "off":
        inp = input("Введите имя студента: ")
        queue.put(inp)
        sleep(2)


def bye(queue):
    while True:
        student = queue.get()
        if student != "":
            print(f"Вы отчислили студента {student}")
        else:
            print("Ошибка - (Себя отчисли)")
        queue.task_done()
        sleep(1)


def main():
    for i in ["Ivanov", "Petrov"]:
        queue.put(i)

    bye_stram = Thread(target=bye, args=(queue,))
    bye_stram.start()

    kik_stram = Thread(target=kick, args=(queue,))
    kik_stram.start()




main()
