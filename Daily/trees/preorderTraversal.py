class Node:
    def __init__(self,data=0,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

def preorderTraversal(root):
    if(not root):
        return None
    else:
        print(root.data)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

root = Node(1)
root.left = Node(2)
root.right  = Node(3)
print(preorderTraversal(root))