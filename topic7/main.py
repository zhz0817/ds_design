def intersection(set1, set2):
    ans = set()
    for info in set1:
        if info in set2:
            ans.add(info)
    return ans


def union(set1, set2):
    ans = set()
    for info in set1:
        ans.add(info)
    for info in set2:
        ans.add(info)
    return ans


def sub(set1, set2):
    ans = set()
    for info in set1:
        if info not in set2:
            ans.add(info)
    return ans


if __name__ == '__main__':
    set1 = set()
    set2 = set()
