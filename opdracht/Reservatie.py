class Reservatie:
    """
    Initializeerd een Reservatie Object
    :param: self, id, userid, timestamp, vertoningid, plaatsen
    :return: reservatie object
    """
    def __init__(self, id, userid, timestamp, vertoningid, plaatsen):
        self.id = id
        self.userid = userid
        self.timestamp = timestamp
        self.vertoningid = vertoningid
        self.plaatsen = plaatsen