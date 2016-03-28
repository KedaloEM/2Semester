
##Корневое дерево
class Node:
    def __init__(self, value):
        self.parent = None
        self.children = []
        self.value = value
        self.left =None
        self.right = None
##Двоичное дерево(потомков не больше двух)
def print_binary_tree(node):
    if not node: #!=None
        return
    print_binary_tree(node.left)
    print(node.value)
    print_binary_tree(node.right)

def tree_search(node, key):
    if not node:
        return None
    if node.key ==key:
        return node
    if key<node.key:
        return tree_search(node.left, key)
    else:
        return tree_search(node.right, key)
## Скорость поиска равна высоте дерева
## N = 2^(n+1) -1




