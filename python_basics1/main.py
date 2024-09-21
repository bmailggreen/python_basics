def print_hi(name):
    print(f'Hi, {name}')


def check5():
    a = input('Kérnék szépen egy számot: ')
    a = int(a)
    #elágazások
    if a == 5:
        print('Az a 5')
    elif a > 5:
        print('Az a nagyobb mint 5')
    else:
        print('Az a kisebb mint 5')



if __name__ == '__main__':
    print_hi('PyCharm')

    a = 5
    b = 3424.234
    c = "asdasasdsa"
    d = 'adfwwerwr'
    e = f'sadasdas'

    print('sdasdasd' + str(a))
    print(f'sadasadsd {a}')

    f = True
    g = False

    #check5()
    #check5()
    #check5()

#    for i in range(0, 3):
#        check5()

#    i = 0
#    while i < 3:
#        check5()
#        i += 1

#for i in range(1, 101):
#    print(i)
