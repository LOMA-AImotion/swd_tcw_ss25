name = input("Wie ist dein Name? ")
alter = int(input("Wie alt bist du? "))

wahl_alter = 18
differenz = alter - wahl_alter

if alter > wahl_alter:
    print(name, "Du darfst seit", differenz, "Jahren wählen.")
elif alter == wahl_alter:
    print("Gratulation,", name, "Du darfst zum ersten Mal wählen.")
else: # z.B. alter = 16 und wahl_alter = 18 
    print(name, "Du musst noch", wahl_alter - alter, "Jahre warten")