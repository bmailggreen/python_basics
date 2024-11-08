#gyumolcsokMennyisege = {
#    'alma': 5,
#    'korte': 10,
#    'szilva': 20
#}

#for kulcs in gyumolcsokMennyisege.keys():
#    print('kulcs: ' + kulcs + ' érték: ' +
#          str(gyumolcsokMennyisege[kulcs]))

szoveg = ("Ez a nap egy olyan nap amikor volt egy pár perc " +
          " szabadidőnk!")
print(szoveg)

gyakorisagTarolo = {}

szavak = szoveg.split(' ')
print(szavak)

for szo in szavak:
    #if szo in szavak.keys():
    if gyakorisagTarolo.get(szo) == None:
        print(gyakorisagTarolo)
        gyakorisagTarolo[szo] = 1
    else:
        gyakorisag = gyakorisagTarolo[szo]
        gyakorisag += 1
        gyakorisagTarolo[szo] = gyakorisag
        print(gyakorisagTarolo)


print(gyakorisagTarolo)


# 1, Csináljatok egy dictionaryt és helyezzetek el
# bele alapból elemeket
# Csak írassátok ki a teljes dictionary tartalmát

# 2, Csináljatok egy üres szótárat.
# Rakjatok bele újabb elemeket,
# bónusz feladat: töröljetek ki belőle
# elemeket.
# Utána szaladjatok végig a kulcsokon és
# írassátok ki a kulcs-érték párokat

# 3, Csináljatok szó gyakorisággal egy szótárat.
# Nézzétek meg hogy az 'az' szó hányszor szerepel
# Ha 3x akkor írjátok ki hogy pont 3x szerepel,
# ha nem akkor meg azt hogy mennyi a különbség
# aközött mint amit elvárnánk és amit találtunk.

# 4, Olvassatok be a 'k' karakter beolvasásáig
# számokat, ha még nem volt beolvasva ez a szám akkor
# rakjátok bele egyes gyakorisággal a számot egy szótárba,
# ha már benne volt, növeljétek eggyel a gyakoriságát.
# Utána írassátok ki a teljes szótár tartalmát.
