def rude_separation (string):
    for i in string:
        if i == ' ':
            i = '|'
        print(i, end='')
    print('\n')
def enter_separation (srting):
    for i in srting:
        if i == ' ':
            i = '\n'
        print(i, end='')
    print('\n')