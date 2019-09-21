#Problem 1
from DoublyLL import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self,elem):
        self.data.add_last(elem)

    def dequeue(self):
        val = self.data.first_node().data
        self.data.delete_first()
        return val


    def first(self):
        return self.data.first_node().data

#Problem 2
















    


    
