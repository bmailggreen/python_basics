# 1, Csináljunk egy fájlt tetszőleges fájlszerkezettel.
# Olvassuk be a tartalmát és rendszerezzük kiírás előtt.
# 2, Keressünk a neten egy szöveges fájlt és írassuk ki a
# tartalmát a képernyőre
# 3, Írjunk ki valamit egy fájlba, írás (w) és hozzáfűzés (a)
# módban is.


if __name__ == '__main__':
    print('Hello World')

file = open('c:/ADATOK/temp/input_adatok_python.csv', 'r')
content = file.readlines()
#print(content)
for line in content:
    #print(line)
    elements = line.split(';')
    #for element in elements:
    #    print(element)
    print(elements)
file.close()

#file2 = open('c:/temp6/out.txt', 'w')
#file2 = open('c:/temp6/out.txt', 'a')
#file2.write('Hello World!\n')
#file2.write('Hello World 2!\n')
#file2.close()


with open('c:/ADATOK/temp/input_adatok_python.csv', 'r') as file:
    content = file.readlines()
    for line in content:
        elements = line.split(';')
        print(elements)

