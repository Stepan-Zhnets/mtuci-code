class Vehicle:
    """
    Базовый класс для транспортных средств.
    Атрибуты:
        make  – марка (строка)
        model – модель (строка)
    """

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def get_info(self) -> str:
        """
        Возвращает строку с информацией о транспортном средстве.
        """
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    """
    Класс автомобиля, наследующий от Vehicle.
    Дополнительно хранит тип топлива (fuel_type).
    """

    def __init__(self, make: str, model: str, fuel_type: str):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self) -> str:
        """
        Переопределённый метод. Добавляет информацию о типе топлива.
        """
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"


# --------------------------------------------------------------------
# Пример использования
if __name__ == "__main__":
    vehicle = Vehicle("Toyota", "Corolla")
    print(vehicle.get_info())          # Марка: Toyota, Модель: Corolla

    car = Car("Ford", "Mustang", "Gasoline")
    print(car.get_info())
    # Марка: Ford, Модель: Mustang, Тип топлива: Gasoline
