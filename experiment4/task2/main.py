class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def rootFirst(root:Tree):
    if root is None:
        return
    print(root.value)
    rootFirst(root.left)
    rootFirst(root.right)


if __name__ == '__main__':
    treeDict = {}
    words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in range(len(words)):
        node = Tree(words[i])
        treeDict[words[i]] = node
    for i in range(10):
        left = i * 2 + 1
        right = i * 2 + 2
        ch = words[i]
        node = treeDict[ch]
        if left < len(words):
            node.left = treeDict[words[left]]
        if right < len(words):
            node.right = treeDict[words[right]]
    root = treeDict[words[0]]
    rootFirst(root)
