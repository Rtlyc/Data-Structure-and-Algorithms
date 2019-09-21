from LinkedBinaryTree import LinkedBinaryTree


node4a = LinkedBinaryTree.Node(4)
node1a = LinkedBinaryTree.Node(1)
node3b = LinkedBinaryTree.Node(3,node4a,node1a)
node1b = LinkedBinaryTree.Node(1)
node6 = LinkedBinaryTree.Node(6,right = node1b)
node4b = LinkedBinaryTree.Node(4,node3b,node6)

tree = LinkedBinaryTree(node4b)
#tree.draw()

def is_sum_balanced(bin_tree):
    boolean,value = is_subtree_sum_balanced(bin_tree.root)
    return boolean

def is_subtree_sum_balanced(subtree_root):
    if subtree_root is None:
        return True,0
    left_bool, left_value = is_subtree_sum_balanced(subtree_root.left)
    right_bool, right_value = is_subtree_sum_balanced(subtree_root.right)
    value = left_value + right_value + subtree_root.data
    boolean = False
    if (left_value - right_value)**2 <= 1:
        boolean = True
    return left_bool and boolean and right_bool , value
#print(is_sum_balanced(tree))


from Stack import ArrayStack

class DupStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.size = 0

    def __len__(self):
        return len(self.size)

    def is_empty(self):
        return len(self) == 0

    def push(self,e):
        if self.is_empty():
            self.stack.push((e,1))
        else:
            prev,dup = self.stack.top()
            if prev == e:
                self.stack.pop()
                self.stack.push((prev,dup+1))
            else:
                self.stack.push((e,1))
        self.size += 1
            

    def top(self):
        if self.is_empty():
            raise Exception("Empty!!")
        return self.stack.top()[0]

    def top_dups_count(self):
        if self.is_empty():
            raise Exception("Empty!!")
        return self.stack.top()[1]

    def pop(self):
        if self.is_empty():
            raise Exception("Empty!!")
        value,count = self.stack.top()
        if count == 1:
            return self.stack.pop()[0]
        else:
            self.stack.pop()
            self.stack.push(value,count-1)
        self.size -= 1

    def pop_dups(self):
        if self.is_empty():
            raise Exception("Empty!!")
        value,count = self.stack.pop()
        self.size -= count
        return value

dupS = DupStack()
dupS.push(4)
dupS.push(5)
dupS.push(5)
dupS.push(5)
dupS.push(4)
dupS.push(4)


def insert_sorted(srt_lnk_lst,elem):
    cur = srt_lnk_lst.first_node()
    while cur.next is not srt_lnk_lst.trailer and cur.data < elem:
        cur = cur.next
    new_node = DoublyLinkedList.Node(elem)
    pred = cur.prev
    new_node.next = cur
    cur.prev = new_node
    new_node.prev = pred
    pred.next = new_node











