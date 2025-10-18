# Задача 1:

print("Задача 1:")
number = int(input("Введите число: "))
for num in range(1, number+1):
    print(num)

print("Задача 2:")
number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))
if number_one > number_two:
    print(f"Большее число: {number_one}")
elif number_one < number_two:
    print(f"Большее число: {number_two}")
else:
    print("Числа равны!")
