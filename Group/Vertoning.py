class Vertoning:
    """
    Initializzerd een object Vertoning
    :param: self, id, zaalnummer, slot, datum, filmid, vrijeplaatsen:
    :return: Verotoning object
    """
    def __init__(self, id, zaalnummer, slot, datum, filmid, vrijeplaatsen):
        pass

    """
    verwijdert een instansie vertoning
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


    def is_empty(vertoningen):
        """"Bepaalt of vertoningen leeg is
        Args:
            vertoningen

        Returns:
            bool true or false"""
        pass


    def get_length(vertoningen):
        """"Geeft de lengte van vertoningen
        Args:
            vertoningen

        Returns:
            int (>= 0)
        """


    def insert(id, lijst):
        """"Voegt een vertoning toe aan de map
        Args:
            id (hash)
            lijst ([zaalnummer, slot, datum, filmid, vrije plaatsen])

        Returns:
            vertoningen met vertoning toegevoegd
        """
        pass


    def delete(id):
        """"verwijderd de vertoning als ze voorbij is: tijd nu < datum
        Args:
            id (hash, int>0)

        Returns:
            vertoning met vertoning verwijderd"""
        pass


    def retrieve(id):
        """"Haalt vertoning op met de unieke ID en geeft de lijst terug
        Args:
            id (hash, int>0)

        Returns:
            vertoningen[id]:
            lijst ([zaalnummer, slot, datum, filmid, vrije plaatsen])
        """
        pass