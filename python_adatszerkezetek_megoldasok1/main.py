# FELADATOK MEGOLDÁSRA:
# 1, Hozzatok létre egy listát felöltve (kezdőértékekkel)
# Nézzeket meg egy-egy elemet az index kiválasztós módszerrel
# pld: lista1[2],  írjatok felül egy-egy element pld:  lista1[2] = 23
# Szaladjatok végig az elemeken és írassátok ki őket
# Írassátok ki egybe a teljes listát
# Kísérletezzetek vele

def elso():
    lista1 = [1, 2, 4, 6, 9, 12, 15, 20, 24]
    print(lista1[2])
    print(lista1[4])
    lista1[2] = 14

    print('\n')
    for element in lista1:
        print(element)

    print(lista1)


# 2, Hozzatok létre egy üres listát.
# Az előző órán megismert módszerrel billentyűzetről
# kérjetek be számokat amíg nem adnak be 'k' karaktert.
# Minden egyes számot tároljatok el a listában.
# Majd írassátok ki a lista tartalmát.


def readNumbersAndGetList():
    lista2 = []
    readInput = ' '
    while True:
        print('Kérem adja meg a következő számot amit el szeretne tárolni!')
        print('Kilépéshez adja meg a k karaktert.')
        readInput = input()
        if readInput == 'k':
            break
        lista2.append(float(readInput))
    return lista2

def masodik():
    lista2 = readNumbersAndGetList()
    print(lista2)

# 3, A második feladatban megismert kóddal létrehozott listán
# szaladjunk végig és adjuk össze a számokat.
def listaOsszege(lista):
    osszeg = 0
    for element in lista:
        osszeg = osszeg + element
    return osszeg

def harmadik():
    lista2 = readNumbersAndGetList()
    osszeg = listaOsszege(lista2)
    print('Az összeg: ' + str(osszeg))

# 4, Ugyanez csak nem az összegre vagyunk kíváncsiak, hanem a
# számtani átlagra. (Összeg / az elemek számával.)
def negyedik():
    lista2 = readNumbersAndGetList()
    osszeg = listaOsszege(lista2)
    osszeg = osszeg / len(lista2)
    print('A számtani átlag: ' + str(osszeg))


# 5, Csináljunk egy programot, ahol egy listában le lehet tárolni a
# billentyűzetről megadott személyneveket és letárolni őket.
def readNamesAndGetList():
    lista2 = []
    readInput = ' '
    while True:
        print('Kérem adja meg a következő nevet amit el szeretne tárolni!')
        print('Kilépéshez adja meg a k karaktert.')
        readInput = input()
        if readInput == 'k':
            break
        lista2.append(readInput)
    return lista2

def otodik():
    lista2 = readNamesAndGetList()
    print(lista2)

# 5a, A legvégén töröljük az összes olyan nevet ami egy politikusnak a
# neve lenne.
def otodikA():
    lista2 = readNamesAndGetList()
    while 'Orbán' in lista2:
        lista2.remove('Orbán')
    while 'Gyurcsány' in lista2:
        lista2.remove('Gyurcsány')
    while 'Simicska' in lista2:
        lista2.remove('Simicska')
    print(lista2)

# 6, Legyen két listánk. Az egyikben vezetéknevek vannak, a másikban
# személynevek. Menjünk végig az összes vezeték és keresztneven és
# minden kombinációban írjuk ki a neveket a képernyőre.
def hatodik():
    vezeteknevek = ['Nagy', 'Kiss', 'Molnár', 'Kovács']
    keresztnevek = ['Krisztián', 'Edit', 'Lajos']

    for vezeteknev in vezeteknevek:
         for keresztnev in keresztnevek:
            print(vezeteknev + ' ' + keresztnev)

hatodik()

