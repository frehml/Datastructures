#https://www.geeksforgeeks.org/doubly-circular-linked-list-set-1-introduction-and-insertion/
#https://www.sanfoundry.com/python-program-implement-circular-doubly-linked-list/
class ListNode:
    """
    initializeerd listnode object
    :param: self, data
    :return: listnode object
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    """
    initializzerd linkedlist object
    :param: self
    :return: linkedlist object
    """
    def __init__(self):
        self.start = None

    """
    insert een node vanvoor in de linkedlist
    :param: node
    :returen: void
    """
    def insert_start(self, node):
        if self.start is None:
            self.start = node
            self.start.next = node
            self.start.prev = node
        else:
            node.next = self.start
            node.prev = self.start.prev
            self.start.prev.next = node
            self.start.prev = node
            self.start = node
    """
    verwijdert een start node
    :param: node
    :return: void
    """
    def delete_start(self):
        if self.start == self.start.next:
            self.start = None
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next
    
    """
    yield elke node in volgorde in de linked list
    :param: self
    :yield: node
    """
    def yields(self):
        node = self.start.next
        yield(self.start.data)

        while(node!=self.start):
            yield node.data
            node = node.next
    
    """
    toont elke node in volgorde in de linked list
    :param: self
    :return: print
    """
    def display(self):
        for ele in self.yields():
            print(ele)
    
    """
    zoekt de node op gegeven index
    :param: self, index
    :return: node
    """
    def get_node(self, index):
        node = self.start
        for i in range(index):
            node = node.next
            
        return node

    def search(self, data):
        node = self.start.next

        while node != self.start:
            if node.data == data:
                return node
            node = node.next

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        if self.start == node:
            self.start = node.next
    
    def delete_data(self, data):
        self.delete_node(self.search(data))
    
    def delete_index(self, index):
        self.delete_node(self.get_node(index))
    """
    toont elke node in volgorde in de linked list in een array
    :param: self
    :return: array
    """
    def save(self):
        array = []
        for ele in self.yields():
            array.append(ele)
        
        return array

