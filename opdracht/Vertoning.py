class Vertoning:
    """
    Initializzerd een object Vertoning
    :param: self, id, zaalnummer, slot, datum, filmid, vrijeplaatsen:
    :return: Verotoning object
    """
    def __init__(self, id, zaalnummer, slot, datum, filmid, vrijeplaatsen):
        self.id = id
        self.zaalnummer = zaalnummer
        self.slot = slot
        self.datum = datum
        self.filmid = filmid
        self.vrijeplaatsen = vrijeplaatsen

    """
    verwijdert een instansie vertoning
    :param: self
    :return: string
    """
    def __del__(self):
        print("\nDeletion of:" + str(self) + ' was succesful')