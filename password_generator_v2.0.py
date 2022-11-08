""" Генератор паролей версия 2.0 """
import secrets
import string

count = int(input("Сколько символов будет содержать пароль? "))
symbols = input("Какие символы будут в пароле: \n"
                "1. Только цифры; \n"
                "2. Только буквы в нижнем регистре; \n"
                "3. Только буквы в верхнем регистре; \n"
                "4. Цифры, буквы в верхнем и нижнем регистрах; \n"
                "5. Цифры, буквы и верхнем и нижнем регистрах и знаки препинания. \n"
                "Ваш выбор цифрой: ")

if symbols == "1": print("Ваш пароль: ", "".join(secrets.choice(string.digits) for i in range(1, count + 1)))
elif symbols == "2": print("Ваш пароль: ", "".join(secrets.choice(string.ascii_lowercase) for i in range(1, count + 1)))
elif symbols == "3": print("Ваш пароль: ", "".join(secrets.choice(string.ascii_uppercase) for i in range(1, count + 1)))
elif symbols == "4": print("Ваш пароль: ", "".join(secrets.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase) for i in range(1, count + 1)))
elif symbols == "5": print("Ваш пароль: ", "".join(secrets.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation) for i in range(1, count + 1)))
else: print("Выбрано неверное действие")
