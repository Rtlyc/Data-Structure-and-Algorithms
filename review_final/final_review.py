from LinkedBinaryTree import LinkedBinaryTree

node4 = LinkedBinaryTree.Node(4)
node1 = LinkedBinaryTree.Node(1)
node8 = LinkedBinaryTree.Node(8)
node6 = LinkedBinaryTree.Node(6,node4,node1)
node7 = LinkedBinaryTree.Node(7)
node4b = LinkedBinaryTree.Node(4,node7,node6)
node10 = LinkedBinaryTree.Node(10)
node5 = LinkedBinaryTree.Node(5,None,node10)
node2 = LinkedBinaryTree.Node(2,node4b,node5)
node19 = LinkedBinaryTree.Node(19,node8)
node13 = LinkedBinaryTree.Node(13)
node9 = LinkedBinaryTree.Node(9,node19,node13)
node5b = LinkedBinaryTree.Node(5,None,node9)
node1 = LinkedBinaryTree.Node(1,node2,node5b)
tree = LinkedBinaryTree(node1)
tree.draw()

def level_list(root,level):
    if root is None:
        return []
    if level == 0:
        return [root.data]
    left = level_list(root.left,level-1)
    right = level_list(root.right,level-1)
    return left + right
#print(level_list(tree.root,6))


from ChainingHashTableMap import ChainingHashTableMap
class PlayList:
    def __init__(self):
        self.hashtable = ChainingHashTableMap()
        self.prev = 0

    def add_song(self,new_song_name):
        self.hashtable[self.prev] = new_song_name
        self.prev = new_song_name
        self.hashtable[new_song_name] = None

    def add_song_after(self,song_name,new_song_name):
        try:
            later = self.hashtable[song_name]
        except:
            raise KeyError("Not Found")
        self.hashtable[new_song_name] = later
        self.hashtable[song_name] = new_song_name
        if later is None:
            self.prev = new_song_name

    def play_song(self,song_name):
        try:
            later = self.hashtable[song_name]
        except:
            raise KeyError("Not Found")
        print(song_name)

    def play_list(self):
        cur = 0
        while cur != None:
            later = self.hashtable[cur]
            if later:
                print(later)
            cur = later

p1 = PlayList()
p1.add_song("Feel It Still")
p1.add_song("Perfect")
p1.add_song("Havana")
p1.add_song_after("Perfect","Thunder")
p1.add_song_after("Feel It Still","Something Just Like This")




















