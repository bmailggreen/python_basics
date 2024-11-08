

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


