class Boock():
    def __init__(self, title:str, author:str, year:int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def get_info(self)->str:
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'

boock = Boock("Блэкаут", "Александр Левченко", 2016)
print(boock.get_info())
