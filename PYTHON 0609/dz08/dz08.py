from Vector2D import *

print("-----------------------------------------------Zadatak-----------------------------------------------")

vec1 = Vector2D(6,3)
vec2 = Vector2D(3,2)
skalar = 3

vecSabiranje = vec1.saberiSa(vec2)
vecOduzimanje = vec1.umanjiZa(vec2)
vecMnozenje = vec1.sklaranoMnozenje(skalar)
vecDeljenje = vec1.sklaranoDeljenje(skalar)

print("Sabiranje vektora je stvorilo vektor({},{})".format(vecSabiranje.x, vecSabiranje.y))
print("Oduzimanje vektora je stvorilo vektor({},{})".format(vecOduzimanje.x, vecOduzimanje.y))
print("Mnozenje skalarom {} je stvorilo vektor({},{})".format(skalar, vecMnozenje.x, vecMnozenje.y))
print("Deljenje skalarom {} je stvorilo vektor({},{})".format(skalar, vecDeljenje.x, vecDeljenje.y))
