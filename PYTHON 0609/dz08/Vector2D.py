import copy
class Vector2D:

    def __init__(self, x,y):
        self.x = x
        self.y = y
        print("Uspesno kreiran vektor({},{})".format(self.x, self.y))

    def saberiSa(self, drugiVektor):
        result = copy.deepcopy(self)
        result.x += drugiVektor.x
        result.y += drugiVektor.y
        return result

    def umanjiZa(self, drugiVektor):
        result = copy.deepcopy(self)
        result.x -= drugiVektor.x
        result.y -= drugiVektor.y
        return result

    def sklaranoMnozenje(self, skalar):
        result = copy.deepcopy(self)
        result.x *= skalar
        result.y *= skalar
        return result

    def sklaranoDeljenje(self, skalar):
        result = copy.deepcopy(self)
        result.x /= skalar
        result.y /= skalar
        return result

