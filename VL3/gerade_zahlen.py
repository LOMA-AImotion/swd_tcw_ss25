# Gib mir die geraden Zahlen zwischen 1 und k aus 
# (k ist eine positive ganze Zahl, die der Benutzer eingibt).

k = int(input("Bitte geben Sie eine positive ganze Zahl ein: "))

for i in range(1, k+1): 
    if i % 2 == 0: 
        print(i)