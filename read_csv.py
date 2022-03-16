from asyncore import read
import csv

def read_csv(file:str, category:str):
    folder = f"data/{category}/hola/{category}"
    f = open(f"{folder}/{file}", encoding="utf-8")
    reader = csv.reader(f)
    data = [row for row in reader]

    print(data[0])

read_csv("museo.csv", "museo")