# 选择排序
from math import inf
from random import random


# 冒泡排序
def bubblesort(s):
    for i in range(len(s) - 1, -1, -1):
        for j in range(0, i):
            if s[j] > s[j + 1]:
                s[j + 1], s[j] = s[j], s[j + 1]


# 直接插入排序
def insertsort(s):
    n = len(s)
    for i in range(1, n):
        x = s[i]
        j = i - 1
        while j >= 0:
            if x <= s[j]:
                s[j + 1] = s[j]
                j -= 1
            else:
                break
        s[j + 1] = x


# 简单选择排序
def selectsort(s):
    for i in range(0, len(s) - 1):
        curmin = inf
        curidx = -1
        for j in range(i, len(s)):
            if s[j] < curmin:
                curmin = s[j]
                curidx = j
        if curidx != -1:
            s[i], s[curidx] = s[curidx], s[i]


# 希尔排序
def shellsort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            x = a[i]
            j = i
            while j >= gap:
                if x < a[j - gap]:
                    a[j] = a[j - gap]
                else:
                    break
                j -= gap
            a[j] = x
        gap //= 2


# 堆排序
def maxheapify(heap, start, end):
    son = start * 2
    while son <= end:
        if son + 1 <= end and heap[son + 1] > heap[son]:
            son += 1
        if heap[son] > heap[start]:
            heap[start], heap[son] = heap[son], heap[start]
            start, son = son, son * 2
        else:
            break


def heapsort(a):
    heap = [None] + a
    root = 1
    l = len(heap)
    for i in range(l // 2, root - 1, -1):
        maxheapify(heap, i, l - 1)
    for i in range(l - 1, root, -1):
        heap[i], heap[root] = heap[root], heap[i]
        maxheapify(heap, root, i - 1)
    return heap[root:]


# 归并排序
def merge(s, start, mid, end):
    tmp = []
    l = start
    r = mid + 1
    while l <= mid and r <= end:
        if s[l] <= s[r]:
            tmp.append(s[l])
            l += 1
        else:
            tmp.append(s[r])
            r += 1
    tmp.extend(s[l:mid + 1])
    tmp.extend(s[r:end + 1])
    for i in range(start, end + 1):
        s[i] = tmp[i - start]


def mergesort(s, start, end):
    if start == end:
        return
    mid = (start + end) // 2
    mergesort(s, start, mid)
    mergesort(s, mid + 1, end)
    merge(s, start, mid, end)


# 快速排序
def quicksortpivot(a, start, end):
    pivot = start
    j = start + 1
    for i in range(start + 1, end + 1):
        if a[i] <= a[pivot]:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[pivot], a[j - 1] = a[j - 1], a[pivot]
    pivot = j - 1
    return pivot


def quicksort(a, start, end):
    if start >= end:
        return
    pivot = quicksortpivot(a, start, end)
    quicksort(a, start, pivot - 1)
    quicksort(a, pivot + 1, end)


if __name__ == '__main__':
    pass


