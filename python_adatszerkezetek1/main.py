

a = 34
b = "asdasdasd"
c = 34.2
d = True

e = 34
f = 35
g = 36

z = 123


# LISTÁK

#    0   1   2   3   4
w = [34, 35, 36, 37, 40]

print(w)
print( w[0] )

zs = w[0] + w[1]

w[0] = 90

print('zs: ' + str(zs))

#w[5] = 123
w.append(123)
print(w)

lista1 = []
lista1.append(1)
lista1.append(2)
lista1.append(3)
lista1.append("asdasdas")
lista1.append(False)
lista1.remove(3)
lista1.remove('asdasdas')
print(lista1)

lista1.clear()
print(lista1)


# SZÓTÁRAK

myData = {
    0: 1,
    1: 2,
    2: 3,
    3: 'asdads',
    4: False,
    "key1": "value1"
}

print(myData[0])
print(myData[1])
print(myData[2])
print(myData[3])
print(myData[4])
print(myData)
print(myData["key1"])

myData["akarmi"] = "value2"
print(myData)

#print(myData["akarmi2"])
print( myData.get("akarmi2") )

if myData.get("akarmi2") == None:
    print('Most beszúrom az új elemet mert nincs még ilyen kulcs!')
    myData['akarmi2'] = 'value2'
else:
    print('Már létezik ilyen kulcs, nem szúrom be az új elemet!')

print( myData.get("akarmi2") )

# FELADAT 1:

koltesek = [2300, -1000, 4000, 1200, 3400, -10000]
osszeg = 0

for element in koltesek:
    osszeg += element

print("A költések összege: " + str(osszeg))

#for i in range(0, 8):
#    print('Szám: ' + str(i))

#for i in range(0, len(koltesek)):
#    print('Szám: ' + str(i))

#for i in range(0, len(koltesek)):
#    print('Szám a listában: ' + str(koltesek[i]))


#for i in range(0, len(koltesek)):
#    if i % 2 != 0:
#        print('Szám a listában: ' + str(koltesek[i]))


# FELADATOK MEGOLDÁSRA:
# 1, Hozzatok létre egy listát felöltve (kezdőértékekkel)
# Nézzeket meg egy-egy element az index kiválasztós módszerrel
# pld: lista1[2],  írjtaok felül egy-egy element pld:  lista1[2] = 23
# Szaladjatok végig az elemeken és írassátok ki őket
# Írasssátok ki egybe a teljes listát
# Kísérletezzetek vele

# 2, Hozzatok létre egy üres listát.
# Az előző órán megismert módszerrel billentyűzetről
# kérjetek be számokat amíg nem adnak be 'k' karaktert.
# Minden egyes számot tároljatok el a listában.
# Majd írassátok ki a lista tartalmát.

# 3, A második feladatban megismert kóddal létrehozott listán
# szaladjunk végig és adjuk össze a számokat.

# 4, Ugyanez csak nem az összegre vagyunk kíváncsiak, hanem a
# számtani átlagra. (Összeg / az elemek számával.)

# 5, Csináljunk egy programot, ahol egy listában le lehet tárolni a
# billentyűzetről megadott személyneveket és letárolni őket.

# 5a, A legvégén töröljük az összes olyan nevet ami egy politikusnak a
# neve lenne.

# 6, Legyen két listánk. Az egyikben vezetéknevek vannak, a másikban
# személynevek. Menjünk végig az összes vezeték és keresztneven és
# minden kombinációban írjuk ki a neveket a képernyőre.

