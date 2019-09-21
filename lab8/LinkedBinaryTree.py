import turtle
class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = left
            self.right = right
            self.parent = None
            if self.left is not None:
                self.left.parent = self
            if self.right is not None:
                self.right.parent = self

        def __repr__(self):
            return str(self.data)

    def __init__(self,root = None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def subtree_count(self,root):
        if root is None:
            return 0
        count = 1
        count += self.subtree_count(root.left)
        count += self.subtree_count(root.right)
        return count

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def sum_nodes(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self,root):
        if root is None:
            return 0
        s = root.data
        s += self.subtree_sum(root.left)
        s += self.subtree_sum(root.right)
        return s

    def height(self):
        if self.root is None:
            raise Exception("This is not a tree.")
        return self.subtree_height(self.root)

    def subtree_height(self,root):
        if root is None or (root.left is None and root.right is None):
            return 0
        left = self.subtree_height(root.left)
        right = self.subtree_height(root.right)
        return max(left,right) + 1

    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self,root):
        if root is None:
            return
        yield root.data
        yield from self.subtree_preorder(root.left)
        yield from self.subtree_preorder(root.right)
        

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self,root):
        if root is None:
            return
        yield from self.subtree_postorder(root.left)
        yield from self.subtree_postorder(root.right)
        yield root.data

    
    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self,root):
        if root is None:
            return
        yield from self.subtree_inorder(root.left)
        yield root.data
        yield from self.subtree_inorder(root.right)

    def breadth_first(self):
        if self.is_empty():
            return
        q = ArrayQueue()
        q.enqueue(self.root)
        while not q.is_empty():
            cur = q.dequeue()
            yield cur
            if cur.left is not None:
                q.enqueue(cur.left)
            if cur.right is not None:
                q.enqueue(cur.right)

    def __iter__(self):
        for node in breadth_first():
            yield node.data


    def draw(self):
        turtle.tracer(0,0)
        self.subtree_draw(self.root)
        turtle.write(str(self.root.data),align = "center",font = 20)

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
            turtle.write(str(root.left.data),align = "center",font = 20)
            turtle.seth(180+angle)
            turtle.fd(length)
        if root.right is not None:
            right_level = height-self.subtree_height(root.right)
            beta = -10 * right_level
            length = 100 - right_level * 10
            turtle.seth(beta)
            turtle.fd(length)
            self.subtree_draw(root.right)
            turtle.write(str(root.right.data),align = "center",font = 20)
            turtle.seth(180 + beta)
            turtle.fd(length)


##node2 = LinkedBinaryTree.Node(2)
##node3 = LinkedBinaryTree.Node(3)
##node1 = LinkedBinaryTree.Node(1,node2,node3)
##tree = LinkedBinaryTree(node1)
##tree.draw()
        
            



    
