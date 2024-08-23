from math import *


# öncelikle metotlarımızı tanımlayalım

class kup:
    def __init__(self, a):
        self.a = a

    def yuzeyAlani(self):
        return (6 * pow(self.a, 2), "cm^2")

    def hacim(self):
        return (pow(self.a, 3), "cm^3")


class kure:
    def __init__(self, r):
        self.r = r

    def yuzeyAlani(self):
        return ("yüzey alanı:", 4 * pi * pow(self.r, 2), "cm^2")

    def hacim(self):
        return (4 / 3 * pi * pow(self.r, 3), "cm^3")


class silindir:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def yuzeyAlani(self):
        return (2 * pi * pow(self.r,2) + 2 * pi * self.r * self.h, "cm^2")

    def hacim(self):
        return (pi * pow(self.r, 2) * self.h, "cm^3")


# şimdi her bir classa ait nesnelerimizi tanımlayalım.... nesneAdı = classAdı(argümanlar)

kupSeker = kup(2)
koli = kup(50)

futbolTopu = kure(10)
pinponTopu = kure(3)

merdane = silindir(3, 30)
tencere = silindir(15, 20)

# metotlarımızı nesneler üzerinden çağıralım
print(pinponTopu.yuzeyAlani())
print(kupSeker.yuzeyAlani())
