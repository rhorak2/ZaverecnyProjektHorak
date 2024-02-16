#Uživatelské rozhraní pro spuštění programu a interakci s uživatelem
from evidence_pojistencu import EvidencePojistencu

pojistene_osoby = EvidencePojistencu()
# Vytvoření instance pojistene_osoby třídy EvidencePojistencu
volba = 0;

while volba != 4:
    # Cyklus pro zadání volby uživatele. Cyklus končí po zadání volby 4.
    print("----------------------")
    print("Evidence pojištěných")
    print("----------------------")
    print("1 - Vytvořit pojištěného")
    print("2 - Zobrazit seznam pojištěných")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    volba = input("Zadejte volbu: ")
    print()

    if volba == "1":
        # Načtení hodnot pro vytváření pojištěného.
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        jeVekCislo = False
        while not jeVekCislo:
            # Validace vstupních dat u věku. Uživatel musí zadat číslo.
            try:
                vek = int(input("Zadejte věk: "))
                jeVekCislo = True
            except ValueError:
                print("Věk musí být číslo.")
        telefon = input("Zadejte telefonní číslo: ")
        try:
            pojistene_osoby.pridej_pojisteneho(jmeno, prijmeni, vek, telefon)
            # Volání metody pro přidání pojištěného
            print("Pojištěná osoba byla vytvořena. Pokračujte libovolnou klávesou.")
            input()
        except ValueError as e:
            # Zobrazení výjimky v případě prázdných atributů jmeno nebo prijmeni
            print(e)
            print("Pokračujte libovolnou klávesou.")
            input()

    elif volba == "2":
        # Volání metody pro výpis pojištěnců
        pojistene_osoby.zobraz_seznam()
        print("Pokračujte libovolnou klávesou.")
        input()
    elif volba == "3":
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        # Volání metody pro nalezení pojištěného
        pojistene_osoby.vyhledej_pojisteneho(jmeno, prijmeni)
        print("Pokračujte libovolnou klávesou.")
        input()
    elif volba == "4":
        # Konec programu
        break
    else:
        # Vypíše se v případě jiné volby než 1 - 4
        print("Neplatná volba. Zadejte číslo od 1 do 4.\n")