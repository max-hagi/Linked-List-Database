class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def getData(self):
        return self.data

    def __repr__(self):
        return f"{self.data}"


