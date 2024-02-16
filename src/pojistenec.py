class Pojistenec:
    # třída Pojištěnec pro reprezentaci pojištených osob
    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Konstruktor třídy Pojistenec.
        :param jmeno: křestní jméno pojištence
        :param prijmeni: příjmení pojištence
        :param vek: věk pojištence
        :param telefon: telefonní číslo pojištěnce
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon