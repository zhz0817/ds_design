from typing import List


def get_left_child(index: int, tree: List[str]) -> str:
    left_index = 2 * index + 1
    if left_index >= len(tree):
        return "!"
    return tree[left_index]


def get_right_child(index: int, tree: List) -> str:
    right_index = 2 * index + 2
    if right_index >= len(tree):
        return "!"
    return tree[right_index]


if __name__ == '__main__':
    tree = []
    for i in range(10):
        ch = chr(ord('A') + i)
        tree.append(ch)
    print(tree)
    for i in range(10):
        left_child = get_left_child(i, tree)
        right_child = get_right_child(i, tree)
        print(left_child, end='')
        print(right_child)
