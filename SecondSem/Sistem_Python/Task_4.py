""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os

os.mkdir(r"C:\Users\pesk2\OneDrive\Рабочий стол\DZ_pyton\Sistem_Python\task4")
os.chdir(r"C:\Users\pesk2\OneDrive\Рабочий стол\DZ_pyton\Sistem_Python\task4")
text_file = open("answer.txt", "w")
text_file.write("Я большой молодец и выполнил задание")


