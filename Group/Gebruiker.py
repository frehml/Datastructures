import LinkedList

class Gebruiker:
    """
    Initializeerd Gebruiker object
    :param: self, id, voornaam, achternaam, emailadress
    :return: Gebruiker object
    """
    def __init__(self, id, voornaam, achternaam, emailadress):
        pass
    
    """
    Verwijdert een instansie van Gebruiker
    :param: self
    :return: string
    """
    def __del__(self):
        pass

    def create():
        """"creert een map
        Args:

        Returns:
            Empty map"""
        pass


    def destroy():
        """"verwijderd een map
        Args:

        Returns:
                void (removes map)"""
        pass


    def is_empty(gebruikers):
        """"Bepaalt of gebruikers leeg is
        Args:
            gebruikers

        Returns:
            bool true or false"""
        pass


    def get_length(gebruikers):
        """"Geeft de lengte van gebruikers
        Args:
            gebruikers

        Returns:
            int (>= 0)
        """


    def insert(id, lijst):
        """"Voegt een gebruiker toe aan gebruikers
        Args:
            id (hash, int>0)
            lijst ([voornaam, achternaam, email])

        Returns:
            gebruikers met gebruiker toegevoegd
        """
        pass


    def delete(id):
        """"verwijderd de gebruiker uit gebruikers
        Args:
            id (hash, int>0)

        Returns:
            gebruikers met gebruiker verwijderd"""
        pass


    def retrieve(id):
        """"Haalt gebruiker op met de unieke ID en geeft de lijst terug
        Args:
            id (hash, int>0)

        Returns:
            gebruikers[id]:
            lijst ([voornaam, achternaam, email])
        """
        pass