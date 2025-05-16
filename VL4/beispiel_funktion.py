def addiere(zahl, zahl2):
    print("addiere")
    return zahl + zahl2

def multipliziere(zahl, zahl2):
    print("Multipliziere")
    return zahl * zahl2

# :list type-hint bezeichnet einen Hinweis, welcher Datentyp im Parameter
def verdopple_jedes_element(werte: list):
    def verdopple(zahl):
        return 2*zahl
    return [verdopple(i) for i in werte]

import math
def quadratwurzel(zahl):
    return -math.sqrt(zahl), math.sqrt(zahl)

print(addiere(2,5))
print(addiere(3, 10))
print(verdopple_jedes_element([1,2,3]))
print(quadratwurzel(9))
#print(verdopple(10))
neg, pos = quadratwurzel(9)
print(pos)