def say_hi(name: str):
    print("Hi", name)

def sag_servus(name: str):
    print("Servus", name)

if input("Sprache boarisch? (j|n)") == "j":
    begrüßung = sag_servus
else:
    begrüßung = say_hi

begrüßung("Andreas")