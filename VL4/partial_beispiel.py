from functools import partial

def addiere(x: int, y: int) -> int:
    return x + y 

addiere_5 = partial(addiere, 5)
konst_7 = partial(addiere_5, 2)

print(addiere(5, 10))
print(addiere_5(3))
print(konst_7())