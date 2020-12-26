class Film:
    """
    Initialiseerd Film object
    :param: self, id, titel, rating
    :return: Film object
    """
    def __init__(self, id, titel, rating):
        self.id = id
        self.titel = titel
        self.rating = rating

    """
    Verwijdert Film object instansie
    :param: film objects
    :return: string
    """
    def __del__(self):
        print("\nDeletion of:" + str(self) + ' was succesful')