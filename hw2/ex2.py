def describe_person (name, age =30):
    print('Имя:', name, '\n', 'Возраст:', age)
print('Введите имя:', end='')
name = input()
print('Введите возраст:', end='')
age = input()
describe_person(name)
describe_person(name, age)