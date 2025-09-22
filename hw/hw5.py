def check_admin(role):
    def decorator(func):
        def wrapper():
            if role == "админ":
                return func()
            else:
                print("Доступ запрещён")
        return wrapper
    return decorator

@check_admin("арзы")
def delete_user():
   print("Пользователь удалён")


@check_admin("админ")
def add_user():
   print("Пользователь добавлен")

delete_user()  # -> Доступ запрещён
add_user()  # -> Пользователь добавлен


class User:
    def __init__(self, login, role):
        self.login = login
        self.role = role


def check_user_admin(user):
    def decorator(func):
        def wrapper():
            if user.role == "админ":
                return func()
            else:
                print(f"Доступ запрещён для {user.login}")
        return wrapper
    return decorator


class User:
    def __init__(self, login, role):
        self.login = login
        self.role = role


admin = User("Temirlan", "админ")
guest = User("Ardager", "пользователь")


@check_user_admin(admin)
def create_report():
    print("Отчёт создан")


@check_user_admin(guest)
def delete_report():
    print("Отчёт удалён")


create_report()  # -> Отчёт создан
delete_report()  # -> Доступ запрещён для Ardager

