print('Добро пожаловать на сайт army.pro')
print('Для регистрации введите Логин: ')
login = input()

print('Введите пароль: ')
password = input()
print('Повторно введите пароль')
password_again = input()
if password == password_again:
    print('Ваш пароль принят!')
else:
    print('Пароль неверный, попробуйте снова!')

print('Вы успешно зарегистрировались!')
print('Добро пожаловать', login)

print('Для входа введите Ваш логин: ')
login_1 = input()
if login == login_1:
    print('Приве, ', login)
    print('Введите пароль: ')
    password_1 = input()
    if password == password_1:
        print('Вы успешно вошли на сайт army.pro')
    else:
        print('Ошибка, при авторизации')
else:
    print('Вы ввели неверный логин')
