import turtle
class BinarySearchTreeMap:

    class Item:
        def __init__(self,key,value = None):
            self.key = key
            self.value = value

        def __repr__(self):
            return "("+str(self.key) + " : "+ str(self.value)+")"

    class Node:
        def __init__(self,item,left = None,right = None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = None
            if self.left is not None:
                self.left.parent = self
            if self.right is not None:
                self.right.parent = self

        def num_children(self):
            count = 0
            if self.left is not None:
                count += 1
            if self.right is not None:
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.left = None
            self.right = None
            self.parent = None

        def __repr__(self):
            return str(self.item)

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def find(self,key):
        cur = self.root
        while cur is not None:
            if key == cur.item.key:
                return cur
            elif key > cur.item.key:
                cur = cur.right
            else:
                cur = cur.left
        return

    def __getitem__(self,key):
        node = self.find(key)
        if node is None:
            raise KeyError(str(key)+ " is not found in the tree.")
        return node.item.value

    def __setitem__(self,key,value):
        node = self.find(key)
        if node is not None:
            node.item.value = value
        else:
            self.insert(key,value)

    def insert(self,key,value = None):
        new_item = BinarySearchTreeMap.Item(key,value)
        new_node = BinarySearchTreeMap.Node(new_item)
        if self.is_empty():
            self.root = new_node
            self.size += 1
        else:
            cur = self.root
            while cur is not None:
                if key == cur.item.key:
                    return
                elif key > cur.item.key:
                    if cur.right is not None:
                        cur = cur.right
                    else:
                        cur.right = new_node
                        new_node.parent = cur
                        self.size += 1
                        return
                elif key < cur.item.key:
                    if cur.left is not None:
                        cur = cur.left
                    else:
                        cur.left = new_node
                        new_node.parent = cur
                        self.size += 1
                        return

    def __delitem__(self,key):
        node = self.find(key)
        if node is None:
            raise KeyError(str(key) +" is not Found.")
        self.delete_node(node)

    def delete_node(self,node):
        num = node.num_children()
        item = node.item
        if node is self.root:
            if num == 0:
                node.disconnect()
                self.size -= 1
            elif num == 1:
                if node.left is not None:
                    self.root = node.left
                elif node.right is not None:
                    self.root = node.right
                self.root.parent = None
                node.disconnect()
                self.size -= 1
            else:
                max_of_left = self.subtree_max(node)
                node.item = max_of_left.item
                self.delete_node(max_of_left)
        else:
            if num == 0:
                parent = node.parent
                if node is parent.left:
                    parent.left = None
                else:
                    parent.right = None
                node.disconnect()
                self.size -= 1
            elif num == 1:
                parent = node.parent
                if node.left is not None:#只有左边有
                    child = node.left
                else:
                    child = node.right
                child.parent = parent
                if node.left is parent.left:
                    parent.left = child
                else:
                    parent.right = child
                node.disconnect()
                self.size -= 1
            else:
                max_of_left = self.subtree_max(node.left)
                node.item = max_of_left.item
                self.delete_node(max_of_left)

        return item
                                       

    def subtree_max(self,root):
        while root.right is not None:
            root = root.right
        return root

    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self,curr_node):
        if curr_node is None:
            return
        yield from self.subtree_inorder(curr_node.left)
        yield curr_node
        yield from self.subtree_inorder(curr_node.right)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key

    def subtree_height(self,root):
        if root is None:
            return 0
        left_height = self.subtree_height(root.left)
        right_height = self.subtree_height(root.right)
        return max(left_height,right_height)+1

    def draw(self):
        turtle.tracer(0,0)
        self.subtree_draw(self.root)
        turtle.write(str(self.root.item),align = "center",font = 15)

    def subtree_draw(self,root):
        height = self.subtree_height(self.root)
        if root is not None:
            turtle.color("lightgreen")
            turtle.dot(20)
            turtle.color("black")
        if root.left is not None:
            left_level = height-self.subtree_height(root.left)
            angle = -180 + 10 * left_level
            length = 100 - left_level * 10
            turtle.seth(-180 + 10 * left_level)
            turtle.fd(length)
            self.subtree_draw(root.left)
            turtle.write(str(root.left.item),align = "center",font = 15)
            turtle.seth(180+angle)
            turtle.fd(length)
        if root.right is not None:
            right_level = height-self.subtree_height(root.right)
            beta = -10 * right_level
            length = 100 - right_level * 10
            turtle.seth(beta)
            turtle.fd(length)
            self.subtree_draw(root.right)
            turtle.write(str(root.right.item),align = "center",font = 15)
            turtle.seth(180 + beta)
            turtle.fd(length)

bst1 = BinarySearchTreeMap()
lst1 = [20,10,28,8,15,22,50,25]
for i in lst1:
    bst1.insert(i)

bst1.draw()
            
            
                    
        
            
