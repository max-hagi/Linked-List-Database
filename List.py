from Node import Node

class List:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, data):
        temp = Node(data)
        if self.count == 0:
            self.head = temp
            temp.next = None
        elif self.count == 1:
            self.head.next = temp
            temp.next = None
        else:
            cur = self.head
            prev = None
            while cur.next != None:
                prev = cur
                cur = cur.next
            prev.next = temp
            temp.next = cur
            cur.next = None

        self.count += 1

    def __repr__(self):
        s = ""
        cur = self.head
        for i in range(self.count - 1):
            s += f"{cur} "
            cur = cur.next
        s += f"{cur}"
        return s







