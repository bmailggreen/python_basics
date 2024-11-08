# 1, Csináljatok egy dictionaryt és helyezzetek el
# bele alapból elemeket
# Csak írassátok ki a teljes dictionary tartalmát
def elso():
    myDict = {
        "alma": "piros",
        "körte": "sárga",
        "szilva": "kék"
    }
    print(myDict)

# 2, Csináljatok egy üres szótárat.
# Rakjatok bele újabb elemeket,
# bónusz feladat: töröljetek ki belőle
# elemeket.
# Utána szaladjatok végig a kulcsokon és
# írassátok ki a kulcs-érték párokat
def masodik():
    szotar = {}
    szotar["uj1"] = 3
    szotar["uj2"] = 30
    szotar["regi1"] = 10
    szotar.pop("regi1")
    for kulcs in szotar.keys():
        print(kulcs + " - " + str(szotar[kulcs]))


# 3, Csináljatok szó gyakorisággal egy szótárat.
# Nézzétek meg hogy az 'az' szó hányszor szerepel
# Ha 3x akkor írjátok ki hogy pont 3x szerepel,
# ha nem akkor meg azt hogy mennyi a különbség
# aközött mint amit elvárnánk és amit találtunk.
def harmadik():
    gyakorisag = {
        'az': 3,
        'a': 10,
        'és': 5
    }
    if gyakorisag.get('az') != None:
        if gyakorisag['az'] == 3:
            print('Pont 3x szerepel!')
        else:
            temp = gyakorisag['az'] - 3
            if temp < 0:
                temp = -1 * temp
            print('Az az gyakoriságának ennyi hiányzik 3-hoz: ' + str(temp))
    else:
        print('Az nincs is benne!')

# 4, Olvassatok be a 'k' karakter beolvasásáig
# számokat, ha még nem volt beolvasva ez a szám akkor
# rakjátok bele egyes gyakorisággal a számot egy szótárba,
# ha már benne volt, növeljétek eggyel a gyakoriságát.
# Utána írassátok ki a teljes szótár tartalmát.
def negyedik():
    szotar = {}
    inputom = ' '
    while True:
        print('Kérem adjon meg egy számot! Kilépéshez a k karaktert!')
        inputom = input()
        if inputom == 'k':
            break
        if szotar.get(inputom) != None:
            gyakorisag = szotar[inputom]
            gyakorisag += 1
            szotar[inputom] = gyakorisag
        else:
            szotar[inputom] = 1
    print(szotar)

negyedik()
