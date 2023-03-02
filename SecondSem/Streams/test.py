"""
Пример для демонстрации потоков, просто запустите и посмотрите как это работает
"""
import time
from threading import Thread


def sleepMe(i=None):
    print(f"Поток {i} засыпает на 5 секунд.\n")
    time.sleep(5)
    print(f"Поток {i} сейчас проснулся.\n")


for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    time.sleep(0.0001)
    th.start()