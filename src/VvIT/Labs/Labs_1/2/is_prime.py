import math
def is_prime(number:int)->bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

num = int(input("Введи число: "))
print(is_prime(num))
