class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def inorderTraversal(root):
    if(root is None):
        return None
    else:
        inorderTraversal(root.left)
        print(root.data)
        inorderTraversal(root.right)


# root = Node(1)
# root.left = Node(2)
# root.right  = Node(3)
# print(inorderTraversal(root))

root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(inorderTraversal(root))