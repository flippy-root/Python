from docx2pdf import convert
import os

# convert(input_path="Мои лайфхаки продуктивности.docx", output_path="мой.pdf")

dir = r"C:\Users\Yuri\Desktop\convert_doc_to_pdf\files"

for file in os.listdir(dir):
    # Добавил функцию replace, чтобы не было повторяющего расширения .docx в выходном файле, об этом в видео забыл упомянуть.
    convert(input_path=rf"{dir}\{file}", output_path=rf"{dir}\{file.replace('.docx', '')}.pdf")
