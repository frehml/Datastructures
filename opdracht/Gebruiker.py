import LinkedList

class Gebruiker:
    """
    Initializeerd Gebruiker object
    :param: self, id, voornaam, achternaam, emailadress
    :return: Gebruiker object
    """
    def __init__(self, id, voornaam, achternaam, emailadress):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.emailadress = emailadress
    
    """
    Verwijdert een instansie van Gebruiker
    :param: self
    :return: string
    """
    def __del__(self):
        print("\nDeletion of:" + str(self) + ' was succesful')