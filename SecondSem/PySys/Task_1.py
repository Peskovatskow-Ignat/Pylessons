"""
Напишите скрипт который выводит надпись "Привет мир" если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. В таком случае выведите надпись "Привет {Имя}"
Пример ввода: python file.py kakoitoArgument --name Oleg(Скрипт должен напечатать привет Oleg)
"""
import sys
if "--name" in sys.argv:
    print("hello",sys.argv[sys.argv.index("--name")+1])
else:
    print("Okey, lets go")

    