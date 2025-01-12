class UserAccount:
    username = None
    email = None
    password = None

    def __init__(self, username, email, password = None):
        self.username = username
        self.email = email
        self.password = password

    def set_password (self):
        print('Установите новый пароль:')
        self.password = input()

    def chek_password (self):
        print('Введите пароль для проверки')
        password = input()
        if self.password == password:
             print( True)
        else:
             print( False)

me = UserAccount('Andrey', 'porosenok@ku.com')
me.set_password()
me.chek_password()
