# 1, Csinálunk egy pár válozót, olvasunk be változókat és konvertáljuk őket,
# majd írjuk ki őket a képernyőre
# 2, Írjunk egy függvényt, ami megkap egy életkort és egy a függvényen belül
# egy elágazás mondja meg hogy az adott személynek szabad-e már autót vezetni
# vagy inni. (16 éves kortól lehet autót vezetni és 18 éves kortól lehet inni.)
# 3, Írjunk egy olyan függvényt, ami kiírja a számokat 1-től 100-ig, de csak a
# páros számokat (if szam % 2 == 0, if szam % 2 != 0) (range(.., .., 2))
# 4, Írjunk függvényt, ami megkap egy számot és megmondja a faktoriálisát


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


def add(a, b):
    return a + b


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

    print('5 + 4: ' + str(add(5, 4)))


