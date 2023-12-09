def display_union(n, intervals):
    # Sort intervals based on their lower bound
    intervals.sort(key=lambda x: x[0])

    # Merge overlapping intervals
    result = [intervals[0]]
    for i in range(1, n):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])

    # Print merged intervals in the standard way
    for i, interval in enumerate(result):
        if i > 0:
            print(" U ", end="")
        if interval[0] == -10**9:
            print("(-inf,", end="")
        elif interval[0] == 10**9:
            print("[inf,", end="")
        else:
            print("[" if interval[2] else "(", end="")
            print(interval[0], end="")
            print(",", end="")
        if interval[1] == -10**9:
            print("-inf)", end="")
        elif interval[1] == 10**9:
            print("inf)", end="")
        else:
            print(interval[1], end="")
            print("]" if interval[3] else ")", end="")

# Read input
n = int(input())
intervals = []
for i in range(n):
    s = input().strip()
    type = s[0]
    if type == '(':
        a, b = map(int, s[1:-1].split(','))
        intervals.append([a+1, b, True, False]) # (a,b)
    elif type == '[':
        a, b = map(int, s[1:-1].split(','))
        intervals.append([a, b, True, True]) # [a,b]
    elif s.startswith('-'):
        a = int(s[6:-1])
        intervals.append([-10**9, a, False, False]) # (-inf,a)
    else:
        a = int(s[1:-7])
        intervals.append([a, 10**9, False, True]) # [a,inf)

# Display union of intervals
display_union(n, intervals)
