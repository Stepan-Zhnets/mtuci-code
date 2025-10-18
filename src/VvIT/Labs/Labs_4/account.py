import hashlib

class UserAccount:
    """
    Класс, представляющий аккаунт пользователя.
    Атрибуты:
        username – имя пользователя (строка)
        email    – электронная почта (строка)
        _password_hash – хэш пароля (приватный атрибут)
    """

    def __init__(self, username: str, email: str, password: str):
        """
        Конструктор. Хеширует пароль сразу при создании аккаунта.

        :param username: имя пользователя
        :param email: электронная почта
        :param password: исходный пароль в виде строки
        """
        self.username = username
        self.email = email
        self._password_hash = self._hash_password(password)

    @staticmethod
    def _hash_password(pwd: str) -> str:
        """Возвращает SHA‑256 хэш пароля."""
        return hashlib.sha256(pwd.encode('utf-8')).hexdigest()

    def set_password(self, new_password: str):
        """
        Изменяет пароль. Сохраняет только его хэш.

        :param new_password: новый пароль
        """
        if not new_password:
            raise ValueError("Пароль не может быть пустым.")
        self._password_hash = self._hash_password(new_password)

    def check_password(self, password: str) -> bool:
        """
        Проверяет, совпадает ли введённый пароль с текущим.

        :param password: проверяемый пароль
        :return: True если пароли совпадают, иначе False
        """
        return self._hash_password(password) == self._password_hash


# --------------------------------------------------------------------
# Пример использования

if __name__ == "__main__":
    # Создаём аккаунт пользователя
    account = UserAccount("alice", "alice@example.com", "initial123")

    # Проверяем исходный пароль
    print("Проверка исходного пароля:", account.check_password("initial123"))  # True

    # Меняем пароль
    account.set_password("new_secure!456")
    print("Пароль изменён.")

    # Тестируем новый пароль
    print("Новый пароль корректен?", account.check_password("new_secure!456"))   # True
    print("Старый пароль ещё работает?", account.check_password("initial123"))  # False
