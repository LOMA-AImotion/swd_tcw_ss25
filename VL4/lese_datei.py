import os # Operating System = Betriebssystem

# os.path.dirname(__file__) gibt mir das Verzeichnis von dieser Datei (lese_datei.py)
print(os.path.dirname(__file__))

# join verknüpft ein Verzeichnis mit einem Dateinamen
adjektive_pfad = os.path.join(os.path.dirname(__file__), 'adjektive.txt')
print(adjektive_pfad)

with open(adjektive_pfad, encoding="utf-8") as datei:
    zeilen = datei.read().splitlines()

print(zeilen)