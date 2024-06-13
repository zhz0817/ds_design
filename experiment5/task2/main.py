class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


is_leaf = {}
degree_dict = {}
level_dict = {}


def count(root: Tree, level: int):
    level_dict[root.value] = level
    degree_dict[root.value] = 0
    if root.left is None and root.right is None:
        is_leaf[root] = True
        return
    if root.left is not None:
        count(root.left, level + 1)
        is_leaf[root] = False
        degree_dict[root.value] += 1
    if root.right is not None:
        count(root.right, level + 1)
        is_leaf[root] = False
        degree_dict[root.value] += 1


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
    count(root, 0)
    count1 = 0
    count2 = 0
    for k, v in is_leaf.items():
        if v:
            count1 += 1
        else:
            count2 += 1
    print("叶子节点数:", count1)
    print("非叶子节点数:", count2)
    print("度统计")
    for word in words:
        print(word, degree_dict[word])
    print("深度统计")
    for word in words:
        print(word, level_dict[word])
