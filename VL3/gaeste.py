gaeste = []

gaeste_befehl = input("Wer kommt? ")
while gaeste_befehl != "niemand":
    gaeste.append(gaeste_befehl)
    gaeste_befehl = input("Wer kommt? ")

print("Es kommen", len(gaeste), "Gäste:",gaeste)