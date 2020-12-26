class Zaal:
    """
    Initializeerd een zaal object
    :param: self, nummer, plaatsen
    :return: zaal object
    """
    def __init__(self, nummer, plaatsen):
        pass
    
    def create_list():
        """"Creert een lijst
        Args:

        Returns:
            Empty list
        """
        pass


    def destroy_list():
        """"Verwijdert lijst
        Args:

        Returns:
            void (removes list)
        """
        pass


    def is_empty(zalen):
        """"Bepaalt of zalen leeg is
        Args:
            zalen

        Returns:
            bool true or false"""
        pass


    def get_length(zalen):
        """"Geeft de lengte van zalen
        Args:
            zalen

        Returns:
            int (>= 0)
        """


    def insert(zaalnummer, zitplaatsen):
        """"Voegt een zaal toe aan de zalen
        Args:
            zaalnummer (>= 0 && <=len(zalen))
            zitplaatsen (>0)

        Returns:
            zalen met de zaal toegevoegd (plaatst zitplaatsen op idx zaalnummer+1 in de zalen)
        """
        pass


    def delete(zaalnummer):
        """"Verwijdert een zaal uit zalen
        Args:
            zaalnummer (>= 0 && <=len(zalen))

        Returns:
            zalen met de zaal verwijderd (verwijdert zaal uit zalen op idx zaalnummer+1)
        """
        pass


    def retrieve(zaalnummer):
        """"Haalt een zaal op met zaalnummer en geeft aantal zitplaatsen terug
        Belangrijkste functie want niet vaak dat er een nieuwe zaal bijkomt of weggaat
        Args:
            zaalnummer (>= 0 && <=len(zalen))

        Returns:
            zalen[zaalnummer+1] (>0)
        """
        pass
