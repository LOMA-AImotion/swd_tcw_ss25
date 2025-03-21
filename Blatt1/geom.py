# a) Möglichst naiv Fläche berechnen
flaeche = 4*3
print(flaeche)

# b) bessere Variablennamen
laenge = 4
breite = 3
flaeche = laenge * breite
print(flaeche)

# c) mit 50 € pro Quadratmeter und 3.5 % Steuer
preis_pro_qm = 50
steuer = 0.035
netto_preis = flaeche * preis_pro_qm
steuerbetrag = netto_preis * steuer
brutto_preis = netto_preis + steuerbetrag
print("Netto:           ", netto_preis)
print("Steuer (3.5 %):  ", steuerbetrag)
print("-----------------")
print("Brutto:          ", brutto_preis)