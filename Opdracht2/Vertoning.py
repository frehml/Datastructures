# map (dictionary) voor vertoning
# dictionary met als key: id en als value een lijst met zaalnummer, slot, datum...
# {id => [zaalnummer, slot, datum, filmid, vrije plaatsen]}

"""vertoningen = {1: [2, "12:00", 12-02-2019, 2, 13]}"""


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
