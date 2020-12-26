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
       self.next = None
       self.prev = None
 
 
class LinkedList:
    """
    initializzerd linkedlist object
    :param: self
    :return: linkedlist object
    """
    def __init__(self):
        self.start = None
        self.count = 0
    
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
    
    """
    insert een node achter een ref node
    :param: ref, new node
    :return: void
    """
    def insert_after(self, ref, node):
        node.next = ref.next
        ref.next.prev = node
        ref.next = node
        node.prev = ref
        self.count += 1

    """
    insert een node achteraan de linkedlsit
    :param: node
    :return: void
    """
    def insert_end(self, node):
        if self.start is None:
            self.start = node
            node.next = node
            node.prev = node
        else:
            self.insert_after(self.start.prev, node)
        
        self.count += 1
    
    """
    insert een node vanvoor in de linkedlist
    :param: node
    :returen: void
    """
    def insert_start(self, node):
        node.next = self.start
        node.prev = self.start.prev

        self.start.prev.next = node
        self.start.prev = node

        self.start = node

        self.count += 1
 
    """
    verwijdert een gegeven node
    :param: node
    :return: void
    """
    def remove(self, node):
        if self.start.next == self.start:
            self.start = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.start == node:
                self.start = node.next

        self.count -= 1
    
    """
    yield elke node in volgorde in de linked list
    :param: self
    :yield: node
    """
    def display(self):
        node = self.start.next
        yield(self.start.data)

        while(node!=self.start):
            yield node.data
            node = node.next

list = LinkedList()
node1 = ListNode(5)
node2 = ListNode(6)
node3 = ListNode(7)

list.insert_end(node1)
list.insert_after(node1, node2)
list.insert_start(node3)

for node in list.display():
    print(node)