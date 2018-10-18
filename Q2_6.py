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

    def isPalindrome(self) :
        stack = []
        node = self
        while node :
            stack.append(node.getVal())
            node = node.getNext()
        node = self
        while node :
            if node.getVal() != stack.pop() :
                return False
            node = node.getNext()
        return True
