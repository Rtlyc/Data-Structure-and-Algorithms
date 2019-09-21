class Node:
    def __init__(self,data = None,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next

    def disconnect(self):
        self.data = None
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.header = Node()
        self.trailer = Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first_node(self):
        if self.is_empty():
            raise IndexError("The list is empty")
        return self.header.next

    def last_node(self):
        if self.is_empty():
            raise IndexError("The list is empty")
        return self.trailer.prev
    
    def add_after(self,node,data):
        new = Node(data,node,node.next)
        node.next.prev = new
        node.next = new
        self.size += 1

    def add_first(self,data):
        self.add_after(self.header,data)

    def add_last(self,data):
        self.add_after(self.trailer.prev,data)

    def add_before(self,node,data):
        self.add_after(node.prev,data)

    def delete_node(self,node):
        k = node.data
        node.next.prev = node.prev
        node.prev.next = node.next
        node.disconnect()
        self.size -= 1
        return k

    def delete_first(self):
        if self.is_empty():
            raise IndexError("The list is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise IndexError("The list is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        if self.is_empty():
            return
        cur = self.header.next
        for i in range(self.size):
            yield cur.data
            cur = cur.next

    def __repr__(self):
        return "["+ "<->".join(str(item) for item in self) + "]"

lnk_lst = DoublyLinkedList()
lnk_lst.add_last(1)
lnk_lst.add_last(2)
lnk_lst.add_last(3)
lnk_lst.add_last(4)
lnk_lst.add_last(5)
lnk_lst.add_first(0)
#print(lnk_lst)
