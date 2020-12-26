import LinkedChain

class LinkedChainTable():
    def __init__(self):
        self.chain = LinkedChain.LinkedChain()

    def tableIsEmpty(self):
        return self.chain.isEmpty()

    def tableLength(self):
        return self.chain.getLength()

    def tableInsert(self, idx, ele):
        return self.chain.insert(idx, ele)

    def tableRetrieve(self, idx):
        return self.chain.retrieve(idx)

    def save(self):
        return self.chain.save()

    def load(self, table):
        return self.chain.load(table)

    def tableDelete(self, ele):
        i = 1
        el = self.chain.first
        while el.data != ele:
            if i > self.tableLength():
                return False

            el = el.next
            i += 1
        return self.chain.delete(i)

        
l = LinkedChainTable()
print(l.tableIsEmpty())
print(l.tableLength())
print(l.tableRetrieve(4)[1])
print(l.tableInsert(4,500))
print(l.tableIsEmpty())
print(l.tableInsert(1,500))
print(l.tableRetrieve(1)[0])
print(l.tableRetrieve(1)[1])
print(l.save())
print(l.tableInsert(1,600))
print(l.save())
l.load([10,-9,15])
l.tableInsert(3,20)
print(l.tableDelete(0))
print(l.save())
print(l.tableDelete(10))
print(l.save())

#True
#0
#False
#False
#True
#True
#500
#True
#[500]
#True
#[600,500]
#False
#[10,-9,20,15]
#True
#[-9,20,15]