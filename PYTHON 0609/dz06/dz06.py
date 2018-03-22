#prvi zadatak
print("Prvi zadatak:")
def calc(x, y, z = "+"):
    if z == "+":
        return x+y
    if z == "*":
        return x*y

x = 2
y = 3

print(calc(x,y))

z = "+"
print(calc(x,y,z))
z = "*"
print(calc(x,y,z))


#drugi zadatak
print("Prvi zadatak:")
def first(x):
    return x[0]
def last(x):
    return x[-1]
def tail(x):
    return x[1:]
def init(x):
    return x[:(len(x)-1)]

niz = [5 , 7 , 2 , 9 , 13]
print(first(niz))
print(last(niz))
print(tail(niz))
print(init(niz))

