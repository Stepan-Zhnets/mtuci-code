def sum_of_two_numbers(num_1:int, num_2:int)->int:
    return num_1 + num_2

if __name__ == "__main__":
    number_one = int(input("Первое число: "))
    number_two = int(input("Второе число: "))
    print(sum_of_two_numbers(number_one, number_two))
