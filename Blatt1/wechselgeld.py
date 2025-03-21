import numpy as np # numeric python
 
rechnungs_betrag = float(input("Wie viel kostet der Artikel? "))
gegebenes_geld = float(input("Wie viel Geld hast du gegeben? "))

if gegebenes_geld > rechnungs_betrag:
    wechsel_geld = gegebenes_geld - rechnungs_betrag
    # runden, um Nachkommastellen nach der 2. Stelle zu ignorieren
    wechsel_geld = np.round(wechsel_geld, 2)
    print("Das Wechselgeld beträgt:", wechsel_geld)
else: 
    print("Du hast zu wenig Geld gegeben. Es fehlen:", np.round(rechnungs_betrag - gegebenes_geld, 2))