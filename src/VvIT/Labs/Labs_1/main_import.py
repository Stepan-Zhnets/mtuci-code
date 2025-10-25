from modules_package import bye, hello

name = str(input("Ваше имя: "))
var = str(input("Команда: "))
def main():
    if var == "Привет":
        hello(name)
    elif var == "Пока":
        bye(name)
    else:
        print("Я вас не понял")

if __name__ == "__main__":
    main()
