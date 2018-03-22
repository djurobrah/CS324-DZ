from Person import *

print("-----------------------------------------------Zadatak1-----------------------------------------------")

person1 = Person("Djurica", "Djuricic", 20)
person2 = Person("Mika", "Mikic", 15)
person3 = Person("Pera", "Peric", 17)

person1.insert()
person2.insert()
person3.insert()

print("Nakog ubacivanja, baza izgleda ovako:")
selectAllResult = person1.selectAll()
for result in selectAllResult:
    print(result)

print("-----------------------------------------------Zadatak2-----------------------------------------------")

def stringIntoList(string):
    string_split = string.split()
    result = []
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = lowercase.upper()
    letters = lowercase + uppercase
    for i in string_split:
        word = ''
        for j in i:
            if j in letters:
                word += j
        if word != '':
            result.append(word)
    return result

string = 'Ova funkcija je superiska, da - jeste!'
string_split = stringIntoList(string)
for k in range(len(string_split)):
    print(string_split[k]);
