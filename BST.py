class Node:
    def __init__(self,key):
        self.val=key
        self.right=None
        self.left=None

def in_order(root):
    if root:
        in_order(root.left)
        print(str(root.val)+"->",end=' ')
        in_order(root.right)
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(str(root.val) + "->", end=' ')
def preorder(root):
    if root:
        print(str(root.val) + "->", end=' ')
        preorder(root.left)
        preorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(in_order(root))
    print(preorder(root),'\n')
    print(post_order(root),'\n')