adjektive = []

eingabe = input("Sag mir ein Adjektiv, ENDE zum Beenden")
while eingabe != "ENDE":
    adjektive.append(eingabe)
    eingabe = input("Sag mir ein Adjektiv, ENDE zum Beenden")

print("Adjektive: ", adjektive)