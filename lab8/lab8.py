#Problem 1
"""
preorder: A B D G C E F H
inorder:  B G D A E C H F
postorder:G D B E H F C A
height: 3
depth of D: 2
"""

#Problem 2
from DoubleLinkedList import DoublyLinkedList
def right_circular_shift(lnk_lst):
    last = lnk_lst.last_node()
    first = lnk_lst.first_node()
    second = first.next
    third = last.prev
    last.next = second
    second.prev = last
    last.prev = lnk_lst.header
    lnk_lst.header.next = last
    first.next = lnk_lst.trailer
    lnk_lst.trailer.prev = first
    first.prev = third
    third.next = first

##lnk = DoublyLinkedList()
##for i in range(10):
##    lnk.add_last(i)
##print(lnk)
##right_circular_shift(lnk)
##print(lnk)

#Problem 3
from LinkedBinaryTree import LinkedBinaryTree

def count_val(root,value):
    if root is None:
        return 0
    count = 0
    if root.data == value:
        count += 1
    count += count_val(root.left,value)
    count += count_val(root.right,value)
    return count

node5 = LinkedBinaryTree.Node(5)
node6 = LinkedBinaryTree.Node(6,node5)

node9 = LinkedBinaryTree.Node(9)
node7 = LinkedBinaryTree.Node(7,node6,node9)
node1 = LinkedBinaryTree.Node(1)
node2 = LinkedBinaryTree.Node(2,node1)
node4 = LinkedBinaryTree.Node(4,node2,node7)

tree = LinkedBinaryTree(node4)
tree.draw()
##print(count_val(tree.root,4))
import turtle,time
#Problem 4
def invert_binary_tree2(bin_tree):
    def invert_helper(root):
        if root is None:
            return
        root.left,root.right = root.right,root.left
        invert_helper(root.left)
        invert_helper(root.right)
    invert_helper(bin_tree.root)


def invert_binary_tree(bin_tree):
    def invert_helper(root):
        if root is None:
            return
        node = LinkedBinaryTree.Node(root.data)
        node.right = invert_helper(root.left)
        node.left = invert_helper(root.right)
        return node
    r = invert_helper(bin_tree.root)
    tree = LinkedBinaryTree(r)
    return tree
        
                
   
tree = invert_binary_tree(tree)
time.sleep(4)
turtle.clear()
tree.draw()

#Problem 5
class LinkedBinaryTree(LinkedBinaryTree):
    def subtree_children_dist(self,root):
        leave_count = 0
        single_count = 0
        both_count = 0
        if root is None:
            return [0,0,0]
        elif root.left is None and root.right is None:
            leave_count += 1
        elif root.left is None:
            single_count += 1
        elif root.right is None:
            single_count += 1
        else:
            both_count += 1
        left_leave,left_single,left_both = self.subtree_children_dist(root.left)
        right_leave,right_single,right_both = self.subtree_children_dist(root.right)
        leave_count += left_leave + right_leave
        single_count += left_single + right_single
        both_count += left_both + right_both
        return [leave_count,single_count,both_count]

##node7 = LinkedBinaryTree.Node(7)
##node8 = LinkedBinaryTree.Node(8)
##node9 = LinkedBinaryTree.Node(9)
##node10 = LinkedBinaryTree.Node(10)
##node5 = LinkedBinaryTree.Node(5)
##node6 = LinkedBinaryTree.Node(6,node9,node10)
##node3 = LinkedBinaryTree.Node(3,node5,node6)
##node4 = LinkedBinaryTree.Node(4,node7,node8)
##node2 = LinkedBinaryTree.Node(2,node4)
##node1 = LinkedBinaryTree.Node(1,node2,node3)
##tree = LinkedBinaryTree(node1)
##tree.draw()
##print(tree.subtree_children_dist(tree.root))



















