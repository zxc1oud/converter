# Проект 5 из 100

import re

celsius = input("Введите C° для конвертирования: ")
celsius = re.search(r'-?\d+\.?\d*', celsius)

if celsius:
   celsius = float(celsius.group())
else:
    print("Введи корректное число.")
    celsius = None

if celsius is not None:
    fahrenheit = celsius * 1.8 + 32
    kelvin = celsius * 1 + 273.15
    reaumur = celsius * 0.8

print(
    "Я конвертировал C° в:\n"
    f"C° → F°: {fahrenheit:.2f}\n"
    f"C° → K: {kelvin:.2f}\n"
    f"C° → R°: {reaumur:.2f}\n"
)