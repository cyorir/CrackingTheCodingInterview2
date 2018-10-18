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

    def partition(self, val) :
        root = self
        node = self
        stack_left = []
        stack_right = []
        while node :
            if node.getVal() < val :
                stack_left.append(node.getVal())
            else :
                stack_right.append(node.getVal())
            node = node.getNext()
        node = root
        while len(stack_left) > 0 :
            node.setVal(stack_left.pop())
            node = node.getNext()
        while node :
            node.setVal(stack_right.pop())
            node = node.getNext()
