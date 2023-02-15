def authenticate(username, password):
    # Предполагаем, что пользователи хранятся в базе данных в виде словаря
    # ключ - это логин пользователя, значение - это пароль
    users = {'pesk2305': 'Oggu1412'}

    # Проверяем, есть ли такой пользователь в базе данных
    if username not in users:
        return False

    # Проверяем, соответствует ли пароль
    if users[username] == password:
        return True

    return False


username = input("Введите логин: ")
password = input("Введите пароль: ")
is_authenticated = authenticate(username, password)
if is_authenticated:
    print("Аутентификация успешна!")
else:
    print("Неправильный логин или пароль")

