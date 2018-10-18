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

    def undup(self) :
        pre = self
        nxt = self.getNext()
        ha = {}
        ha[pre.getVal()] = 1
        while nxt :
            if nxt.getVal() in ha :
                nxt = nxt.getNext()
                pre.setNext(nxt)
            else :
                ha[nxt.getVal()] = 1
                pre = nxt
                nxt = nxt.getNext()
        
