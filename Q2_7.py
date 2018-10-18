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

    def intersection(self, lst) :
        stacka = []
        node = self
        while node :
            stacka.append(node)
            node = node.getNext()
        stackb = []
        node = lst
        while node :
            stackb.append(node)
            node = node.getNext()
        intersection = stacka[-1]
        while len(stacka) > 0 and stacka[-1] == stackb[-1] :
            intersection = stacka.pop()
            stackb.pop()
        return intersection
