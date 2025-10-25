# Открытие и чтение файла
try:
    with open('example_.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"Ошибка: {e}")

# Построчное чтение
try:
    with open('example_.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
