import os

count = 1

# Путь к вашей папке.
dir = r"C:\Python project\rename\Новая папка"
for file in os.listdir(dir):
    os.rename(rf"{dir}\{file}", rf"{dir}\{count}.txt")
    count += 1
