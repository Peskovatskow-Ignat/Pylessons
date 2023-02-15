"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""

import os

os.mkdir(r"C:\Users\pesk2\OneDrive\Рабочий стол\DZ_pyton\Sistem_Python\target")
os.chdir(r"C:\Users\pesk2\OneDrive\Рабочий стол\DZ_pyton\Sistem_Python\target")

for i in range(1, 11):
    os.mkdir(f"{i}")

