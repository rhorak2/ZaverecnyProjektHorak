from pojistenec import Pojistenec
class EvidencePojistencu:
    # třída pro správu seznamu pojištěnců

    def __init__(self):
        # Konstruktor třídy, který vytváří prázdný seznam pojisteni pro ukládání informací o pojištěncích.
        self.pojisteni = []

    def pridej_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        """
        Metoda určená pro přidání nového pojištěného do seznamu pojistěných
        :param jmeno: křestní jméno pojištence
        :param prijmeni: příjmení pojištence
        :param vek: věk pojištence
        :param telefon: telefonní číslo pojištěnce
        :raises ValueError: Nelze zadat pojišťence bez jména či příjmení
        """
        if not jmeno or not prijmeni:
            raise ValueError("Jméno ani příjmení nesmí být prázdné.\n")

        pojisteny = Pojistenec(jmeno, prijmeni, vek, telefon)
        # vytvoří instanci pojisteny třídy Pojistenec
        self.pojisteni.append(pojisteny)

    def zobraz_seznam(self):
        # Metoda pro výpis všech pojištěnců.
        if not self.pojisteni:
            # Kontrola zda seznam pojištěnců obsahuje nějaké záznamy.
            print("Nebyl nalezen žádný pojištěnec.\n")
        else:
            print("Seznam pojištěných:")
            for pojisteny in self.pojisteni:
                # for cyklus pro výpiš všech pojištěnců
                print(f"\nJméno: {pojisteny.jmeno}")
                print(f"Příjmení: {pojisteny.prijmeni}")
                print(f"Věk: {pojisteny.vek}")
                print(f"Telefon: {pojisteny.telefon}")

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        """
        Metoda pro vyhledání pojištěného podle jména a příjmení.
        :param jmeno: křestní jméno pojištence
        :param prijmeni: příjmení pojištence
        """
        for pojisteny in self.pojisteni:
            # for cyklus pro procházení seznamu pojištěných
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                # Kontrola zda je hledaný pojištěný v seznamu pojištěnců
                print(f"\nJméno: {pojisteny.jmeno}")
                print(f"Příjmení: {pojisteny.prijmeni}")
                print(f"Věk: {pojisteny.vek}")
                print(f"Telefon: {pojisteny.telefon}")
            else:
                print(f"Pojištěný {jmeno} {prijmeni} nebyl nalezen.")
