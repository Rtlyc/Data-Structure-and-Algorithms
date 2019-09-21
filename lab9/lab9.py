#Problem 1
from BinarySearchTreeMap import BinarySearchTreeMap
def are_bst_keys_same(bst1,bst2):
    d = {}
    for i in bst1:
        d[i] = 1
    for i in bst2:
        try:
            d[i]
            return True
        except:
            continue
    return False

bst1 = BinarySearchTreeMap()
lst1 = [20,10,28,8,15,22,50,25]
for i in lst1:
    bst1.insert(i)

#bst1.draw()
bst2 = BinarySearchTreeMap()
lst2 = [20,8,22,15,25,10,50,28]
for i in lst2:
    bst2.insert(i)
#bst2.draw()
#print(are_bst_keys_same(bst1,bst2))

#Problem 2

def is_bst(binary_tree):
    root = binary_tree.root.item.key
    def is_bst_helper(subtree_root):
        if subtree_root is None:
            return True,root,root
        left_bool,left_min,left_max = is_bst_helper(subtree_root.left)
        right_bool,right_min,right_max = is_bst_helper(subtree_root.right)
        boolean = True
        cur_min = min(subtree_root.item.key,left_min,right_min)
        cur_max = max(subtree_root.item.key,left_max,right_max)
        if cur_min != left_min or cur_max != right_max:
            boolean = False
        return boolean,cur_min,cur_max
    return is_bst_helper(binary_tree.root)[0]

##bst2.root.right.item.key = 0
##bst2.draw()
##print(is_bst(bst2))
    
#Problem 3

def lca_bst(bst,node1,node2):
    cur1 = node1
    cur2 = node2
    if cur1.item.key > cur2.item.key:
        cur1,cur2 = cur2,cur1
    key1,key2 = cur1.item.key,cur2.item.key
    if key1 <= bst.root.item.key <= key2:
        return bst.root
    while cur1 is not bst.root:
        if cur1.item.key == key2:
            return cur1
        elif key1 < cur1.item.key < key2:
            answer = cur1
            break
        else:
            cur1 = cur1.parent
    while cur2 is not bst.root:
        if cur2.item.key == key1:
            return cur2
        cur2 = cur2.parent
    return answer

bst = BinarySearchTreeMap()
lst = [18,10,42,15,25,81,33,67,90,28,97]
for i in lst:
    bst.insert(i)
bst.draw()
node1 = bst.root.right.right
node2 = bst.root.right.right.left
print(node1,node2)
print(lca_bst(bst,node1,node2))

def lca_bt(bt,node1,node2):
    cur1 = node1
    cur2 = node2
    d = {}
    while cur1 is not bt.root:
        d[cur1] = 1
        cur1 = cur1.parent
    while cur2 is not bt.root:
        try:
            d[cur2]
            return cur2
        except:
            cur2 = cur2.parent
    return bt.root

from LinkedBinaryTree import LinkedBinaryTree
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
##print(lca_bt(tree,node9,node5))

        












    
