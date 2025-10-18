print("Работа с аргументами функций:")
def describe_person(name:str, age:int =30)->None:
    print(f"""
_____________________
|Имя человека: =====> {name}
|Возраст человека: => {age}
""")
input_name = str(input("Введите имя: "))
describe_person(input_name)
