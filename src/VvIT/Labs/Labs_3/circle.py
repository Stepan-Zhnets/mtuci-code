class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        """Возвращает текущий радиус."""
        return self.radius

    def set_radius(self, new_radius: float):
        """Устанавливает новый радиус."""
        if new_radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.radius = new_radius

# Пример использования
if __name__ == "__main__":
    # Создаём объект круга с начальным радиусом 5.0
    circle = Circle(5.0)
    print(f"Начальный радиус: {circle.get_radius()}")
    # Меняем радиус на 10.5
    circle.set_radius(10.5)
    # Выводим новый радиус
    print(f"Новый радиус: {circle.get_radius()}")
