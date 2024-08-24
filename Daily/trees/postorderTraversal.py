class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def postorderTraversal(root):
    if(not root):
        return
    else:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data)

root = Node(1)
root.left = Node(2)
root.right  = Node(3)
print(postorderTraversal(root))
