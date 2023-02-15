"""
Номер билета 5
"""

import random
import time


class Talking:

    def __init__(self, name=None, count_y=0, count_n=0):
        self.name = name
        self.count_y = count_y
        self.count_n = count_n

    def to_answer(self):
        return f"Имя котёнка {self.name}"

    def number_yes(self):
        self.count_y += 1
        return f"{cat.name} произносит - {list_1[0]}: {self.count_y} раз"

    def number_no(self):
        self.count_n += 1
        return f"{cat.name} произносит - {list_1[1]}: {self.count_n} раз"


list_1 = ["moore-moore", "meow-meow"]
cat = Talking()
print(f"{cat.to_answer()} у него сегодня хорошее настроение и он делает следующте вещи:")
time.sleep(3)
print(cat.number_yes())
time.sleep(2)
count = 1
while True:
    i = random.randint(1, 2)
    if i > count:
        print(cat.number_yes())
    else:
        print(cat.number_no())
    time.sleep(1)
