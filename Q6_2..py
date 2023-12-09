n = int(input())
p = [int(input()) for i in range(n)]


def merge_sort(l, r):
    if r - l <= 1:
        return 0

    mid = (l + r) // 2
    cnt = merge_sort(l, mid) + merge_sort(mid, r)

    i = l
    j = mid
    q = []

    while i < mid or j < r:
        if j == r or (i < mid and p[i] < p[j]):
            q.append(p[i])
            i += 1
        else:
            cnt += mid - i
            q.append(p[j])
            j += 1

    p[l:r] = q

    return cnt


print(merge_sort(0, n))
