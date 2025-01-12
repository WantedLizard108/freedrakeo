def read(file, filename, choose):
    file = open(filename, 'r')
    if choose == 1:
        print(file.read())
    else:
        for line in file:
            print(line, end='')

file = open('example.txt', 'w')
file.write('i am giant\ni am tiny\ni am strong\ni am weak')
file.close()
b= False

while b==False:
    try:
        print('Введите название файла:\n')
        filename = input()
        print('Укажите цифрой, каким способом вы хотите открыть файл.\n 1.Целиком\n 2.Построчно ')
        choose = int(input())
        read(file, filename, choose)
        b=True
    except FileNotFoundError:
        print('Вы ввели название несуществующего файла!')
    finally:
        file.close()
