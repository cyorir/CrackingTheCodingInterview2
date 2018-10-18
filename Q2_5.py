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

    def setVal(self, val) :
        self.val = val

    def listToNum(self) :
        output = 0
        node = self
        while node :
            output *= 10
            output += node.getVal()
            node = node.getNext()
        return output

def numToList(num) :
    lst = LinkedList(num % 10)
    num //= 10
    while num > 0 :
        tmp = lst
        lst = LinkedList(num % 10)
        lst.setNext(tmp)
        num //= 10
    return lst

def sumLists(a,b) :
    return numToList(a.listToNum()+b.listToNum())
        
    
