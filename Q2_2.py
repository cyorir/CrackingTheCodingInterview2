class LinkedList :
    def __init__(self, val) :
        self.val = val
        self.next = None

    def add(self, val) :
        if self.next == None :
            self.next = LinkedList(val)
        else :
            self.next.add(val)

    def getNext(self) :
        return self.next

    def setNext(self, nxt) :
        self.next = nxt

    def getVal(self) :
        return self.val

    def getLen(self) :
        node = self
        ct = 0
        while node :
            ct += 1
            node = node.getNext()
        return ct

    def kFromLast(self, k) :
        le = self.getLen()
        if k > le :
            return -1
        node = self
        while k < le :
            node = node.getNext()
            le -= 1
        return node
