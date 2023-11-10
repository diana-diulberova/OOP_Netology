f = open('hello.txt')
print(type(f))

# прочитаем файл
data = f.read()
print(data, type(data))

# закроем файл
f.close()

# это менеджер контекста
with open('text.txt', encoding='utf-8') as f:
    data = f.read()
    print(type(f))
    print(data)
# Функция read читает весь файл целиком

with open('text.txt', encoding='utf-8') as f:
    data += '\nЕще одна строка'
    print(data)

# Функция readline читает одну строку
# Функция strip удаляет все непечатные символы. В нашем случае - перенос строки
with open('text.txt', encoding='utf-8') as f:
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())

# Функция readlines читает текст в список
with open('text.txt', encoding='utf-8') as f:
    lines = f.readlines()
    print(type(lines))
    print(len(lines))
    print(lines[1])

# Итерироваться по строкам
with open('text.txt', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
# Итерироваться как по списку (по ключу и по индексу)
with open('text.txt', encoding='utf-8') as f:
    for idx, l in enumerate(f):
        print(idx, l.strip())


# Записать в файл
with open('test.txt', 'w') as f:
    f.write('Test 1')
with open('test.txt', 'w') as f:
    f.write('Test 2\n')
# Прочитать из файла
with open('test.txt', 'r') as f:
    print(f.read())

# Дописать в файл
with open('test.txt', 'a') as f:
    f.write('Test 3')
with open('test.txt', 'r') as f:
    print(f.read())
