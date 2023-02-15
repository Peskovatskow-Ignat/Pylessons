import os

def sodanie_papok():
    for i in range(10):
        os.mkdir(fr"123{i}")
        os.chdir(fr"123{i}")
        for j in range(10):
            test_txt = open(f"2323{j}", "w")