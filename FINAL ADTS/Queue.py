class Queue:
    """
    creert een lege queue
    :param: self
    :return: Queue class
    """
    def __init__(self):
        self.end = None
        self.next = None

    def isEmpty(self):
        if self.end is None:
            return True
        return False

    """
    voegt een element toe aan de queue
    :param: self, ele
    :return: void
    """
    def enqueue(self, ele):
        n = Queue()
        n.end = self.end
        n.next = self.next

        self.next = n
        self.end = ele
        return True

    """
    verwijdert het eerste element dat in de queue is toegevoegd
    :param: self
    :return: void
    """
    def dequeue(self):
        if self.next is None:
            return [None, False]

        if self.next.next is None:
            self.next = None
            return [self.end, True]
        
        return self.next.dequeue()

    """
    vraagt het eerste toegevoegde element in de queue op
    :param: self
    :return: het eerste element in de queue
    """
    def getFront(self):
        if self.next is None:
            return [None, False]
        
        if self.next.next is None:
            return [self.end, True]
        
        return self.next.getFront()

    def load(self, array):
        self.end = None
        self.next = None

        for ele in array[::-1]:
            self.enqueue(ele)
    
    def save(self):
        array = []
        el = self.dequeue()
        while (el[1]):
            array.append(el[0])
            el = self.dequeue()

        self.load(array[::-1])
        return array[::-1]

q = Queue()
print(q.isEmpty())
print(q.getFront()[1])
print(q.dequeue()[1])
print(q.enqueue(2))
print(q.enqueue(4))
print(q.isEmpty())
print(q.dequeue()[0])
q.enqueue(5)
print(q.save())
q.load(['a', 'b', 'c'])
print(q.save())
print(q.dequeue()[0])
print(q.save())
print(q.getFront()[0])
print(q.save())