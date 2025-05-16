def flaeche(breite, hoehe, preis = 5, steuersatz=1.19):
    a = breite * hoehe
    gesamtpreis = preis*a*steuersatz
    return gesamtpreis

print(flaeche(10, 10))
# mehrdeutig falls steuersatz keinen Standardwert hätte
print(flaeche(10, 10, 5))
print(flaeche(10, 10, steuersatz=1.07))
print(flaeche(10, 10, preis=4))