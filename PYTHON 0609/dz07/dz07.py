print("-----------------------------------------------Prvi zadatak-----------------------------------------------")
def funkcija(a,b):
    if a < b:
        return a+b
    else:
        return a*b

print(funkcija(2,3))
print(funkcija(3,2))


print("-----------------------------------------------Drugi zadatak-----------------------------------------------")
def increment(niz):
    result = []
    for i in range(len(niz)):
        result.append(niz[i] + 1)
    return result

niz = [1 , 5 , 7 , 8, 2]
niz2 = increment(niz)
print("niz:")
for i in range(len(niz)):
    print(niz[i], end=" ")
print("\n uvecan niz:")
for i in range(len(niz2)):
    print(niz2[i], end=" ")


print("\n -----------------------------------------------Treci zadatak-----------------------------------------------")
def sabira(x,y,i = 0):
    if(len(x) != len(y)):
        try:
            import time
            time.sleep(1)
            raise RuntimeError('Liste su različitih dužina.')
        except RuntimeError as e:
            print('Don\'t do it pls.')
            return
    if i < len(x):
        return [x[i] + y[i]] + sabira(x, y, i + 1)
    else:
        return []

niz = [1 , 2 , 2 , 1]
niz2 = [1 , 2 , 3, 4]
niz3 = [1 , 2 , 3 , 4 , 5]
niz_sabran = sabira(niz, niz2)
niz_nikakav = sabira(niz, niz3)

print("\n prvi niz:")
for i in range(len(niz)):
    print(niz[i], end=" ")
print("\n drugi niz:")
for i in range(len(niz2)):
    print(niz2[i], end=" ")
print("\n treci niz:")
for i in range(len(niz3)):
    print(niz3[i], end=" ")
print("\n sabran niz:")
for i in range(len(niz_sabran)):
    print(niz_sabran[i], end=" ")



