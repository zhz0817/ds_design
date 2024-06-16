from typing import List


def add(a: List, b: List):
    index1 = len(a) - 1
    index2 = len(b) - 1
    ans = []
    while index1 >= 0 and index2 >= 0:
        exponent1 = a[index1][1]  # 指数
        coefficient1 = a[index1][0]  # 系数
        exponent2 = b[index2][1]  # 指数
        coefficient2 = b[index2][0]  # 系数
        if exponent1 > exponent2:
            ans.append(b[index2])
            index2 -= 1
        elif exponent1 < exponent2:
            ans.append(a[index1])
            index1 -= 1
        else:
            ans.append([coefficient1 + coefficient2, exponent1])
            index1 -= 1
            index2 -= 1
    while index1 >= 0:
        ans.append(a[index1])
        index1 -= 1
    while index2 >= 0:
        ans.append(b[index2])
        index2 -= 1
    ans.reverse()
    return ans


if __name__ == '__main__':
    a = [[3, 3], [5, 2], [1, 1], [4, 0]]  # 3x**3 + 5x**2+x+4
    b = [[1, 4], [0, 3], [2, 2], [3, 1], [2, 0]]  # x**4+2x**2+3x+2
    ans = add(a, b)
    print(ans)
