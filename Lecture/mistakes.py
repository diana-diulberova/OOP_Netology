import os
#  Для работы с путями до файлов используется библиотека os

# Получить абсолютный путь к текущей директории
print(os.getcwd())

# Построить путь к файлу из корня
file_path = os.path.join(os.getcwd(), 'test.txt')
print(file_path)
