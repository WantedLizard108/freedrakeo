file= open('example.txt', 'w')
file.write('i am giant\ni am tiny\ni am strong\ni am weak')
file.close()
def read (file, choose):
    file = open('example.txt', 'r')
    if choose == 1:
        print(file.read())
    else:
        for line in  file:
            print(line, end ='')
    file.close()
print('Укажите цифрой, каким способом вы хотите открыть файл.\n 1.Целиком\n 2.Построчно ')
choose = int(input())
read(file, choose)