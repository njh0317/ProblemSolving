import sys
sys.setrecursionlimit(10000)

answer = [[],[]]

class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    global answer
    def __init__(self):
        self.root = None
        
    def insert(self, data, key):
        self.root = self._insert(self.root, data, key)
        return self.root is not None
    
    def _insert(self, node, data, key):
        if node is None:
            node = Node(data, key)
        else:
            if data < node.data:
                node.left = self._insert(node.left, data, key)
            else:
                node.right = self._insert(node.right, data, key)
        return node
    
    def preorder_traverse(self, node):
        if node is None:
            return
        answer[0].append(node.key)
        self.preorder_traverse(node.left)
        self.preorder_traverse(node.right)
    
    def postorder_traverse(self, node):
        if node is None:
            return
        self.postorder_traverse(node.left)
        self.postorder_traverse(node.right)
        answer[1].append(node.key)

def solution(nodeinfo):
    global answer
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort(key = lambda x: (-x[1], x[0]))
    
    bst = BinarySearchTree()
    for node in nodeinfo:
        bst.insert(node[0], node[2])  #x, key
    bst.preorder_traverse(bst.root)
    bst.postorder_traverse(bst.root)
    
    return answer