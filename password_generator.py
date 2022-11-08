""" Генератор паролей версия 1.0 """

from random import randint

symbols = int(input("Введите, сколько символов будет содержать пароль: "))
passwords = ""

for i in range(1, symbols + 1):
    temp = randint(1, 10)
    passwords += str(temp)

print(f"Ваш пароль: {passwords}")
