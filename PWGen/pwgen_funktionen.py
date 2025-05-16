import random 

def lese_datei(datei_name: str) -> list:
    """liest eine Textdatei und liefert die Zeilen als Strings
    in einer Liste

    Args:
        datei_name (str): der Dateiname der zu ladenden Datei

    Returns:
        list: eine Liste von Strings mit den Zeilen 
    """
    with open(datei_name, encoding="utf-8") as datei:
        zeilen = datei.read().splitlines()
    return zeilen

def generiere_passwort(adjektive_datei: str, nomen_datei: str) -> str:
    adjektive = lese_datei(adjektive_datei)
    nomen = lese_datei(nomen_datei)
    # ziehe Adjektiv
    adjektiv = random.choice(adjektive)
    # ziehe Nomen
    gew_nomen = random.choice(nomen)
    
    # ziehe Zahl zw. 0 und 100
    zahl = random.randint(0, 100)
    # ziehe Sonderzeichen
    sonderzeichen = random.choice("*~%&$§")
    # kombiniere und gib zurück 
    return adjektiv + gew_nomen + str(zahl) + sonderzeichen
    

import os
adjektive_pfad = os.path.join(os.path.dirname(__file__), "adjektive.txt")
nomen_pfad = os.path.join(os.path.dirname(__file__), "nomen.txt")

print(generiere_passwort(adjektive_datei=adjektive_pfad, nomen_datei=nomen_pfad))