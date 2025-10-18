# -*- coding: utf-8 -*-

class Employee:
    def __init__(self, name: str, emp_id: int):
        self.name = name
        self.emp_id = emp_id

    def get_info(self) -> str:
        return f"ID: {self.emp_id}, Имя: {self.name}"


class Manager(Employee):
    def __init__(self, name: str, emp_id: int, department: str):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self, project_name: str) -> str:
        return f'{self.name} руководит проектом "{project_name}" в отделе {self.department}'


class Technician(Employee):
    def __init__(self, name: str, emp_id: int, specialization: str):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, task: str) -> str:
        return f'{self.name} (специализация: {self.specialization}) выполняет задачу: {task}'


class TechManager(Manager):          # наследуем только от Manager
    def __init__(self, name: str, emp_id: int,
                 department: str, specialization: str):
        # явно вызываем конструктор Manager (а тот уже вызовет Employee)
        super().__init__(name, emp_id, department)

        # собственное свойство – специализация
        self.specialization = specialization

        # список подчинённых
        self.team = []

    def add_employee(self, employee: Employee) -> None:
        if not isinstance(employee, Employee):
            raise TypeError("add_employee ожидает объект класса Employee")
        self.team.append(employee)

    def get_team_info(self) -> str:
        if not self.team:
            return f"{self.name} пока не имеет подчинённых."
        lines = [f"Команда {self.name}:"]
        for emp in self.team:
            lines.append(f"  - {emp.get_info()}")
        return "\n".join(lines)

    # Можно добавить собственный метод, если нужен
    def perform_maintenance(self, task: str) -> str:
        return f'{self.name} (специализация: {self.specialization}) выполняет задачу: {task}'



# --------------------------------------------------------------------
# Демонстрация работы

if __name__ == "__main__":
    # Создаём базового сотрудника
    emp = Employee("Андрей", 1001)
    print(emp.get_info())
    print()

    # Менеджер
    mgr = Manager("Елена", 2002, "Маркетинг")
    print(mgr.get_info())
    print(mgr.manage_project("Новый рекламный кампейн"))
    print()

    # Техник
    tech = Technician("Игорь", 3003, "Сетевые технологии")
    print(tech.get_info())
    print(tech.perform_maintenance("Обновление роутера"))
    print()

    # TechManager – сочетание ролей
    tm = TechManager("Мария", 4004, "ИТ-отдел", "Разработка ПО")
    print(tm.get_info())
    print(tm.manage_project("Внедрение новой CRM"))
    print(tm.perform_maintenance("Диагностика сервера"))
    print()

    # Добавляем сотрудников в команду TechManager
    tm.add_employee(emp)
    tm.add_employee(mgr)
    tm.add_employee(tech)

    # Выводим информацию о команде
    print(tm.get_team_info())
