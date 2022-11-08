import shutil
import os

diroctory = r"C:\Python project\Console\file filter"

docs = r"C:\Python project\Console\file filter\Документы"
images = r"C:\Python project\Console\file filter\Изображения"
music = r"C:\Python project\Console\file filter\Музыка"

for file in os.listdir(diroctory):
    ext = os.path.splitext(file)[1]
    match ext.lower():
        case ".png":
            shutil.move(src=rf"{diroctory}\{file}", dst=images)
        case ".docx":
            shutil.move(src=rf"{diroctory}\{file}", dst=docs)
        case ".mp3":
            shutil.move(src=rf"{diroctory}\{file}", dst=music)
