import math


def min_max_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, cnt_left = min_max_sort(arr[:mid])
    right, cnt_right = min_max_sort(arr[mid:])
    cnt = cnt_left + cnt_right

    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            cnt += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return merged, cnt


n = int(input())
arr = [int(input()) for _ in range(n)]

_, cnt = min_max_sort(arr)
print(cnt)
