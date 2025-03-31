class User:
    def __init__(self, id: int, username: str, email: str, password_hash: str, role: str):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role  # Добавлено новое поле

    def get_role(self) -> str:
        return self.role  # Новый геттер для роли пользователя