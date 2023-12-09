from queue import Queue

# تعریف یک نماد برای مانترل پذیر نبودن راه حل
INF = int(1e9)


def is_valid(x, y, n, m):
    # شرط مورد نظر برای اعتبار سنجی خارج شدن از مستطیل
    return x >= 0 and x <= n and y >= 0 and y <= m


def bfs(src_i, src_j, des_i, des_j, grid):
    # تعریف صف برای جستجوی سطح به سطح
    q = Queue()
    q.put((src_i, src_j, 0))

    # تعریف دیکشنری برای ذخیره‌ی تعداد تغییرات لازم برای رسیدن به هر گره
    # مقدار اولیه برای همه گره‌ها برابر با بی‌نهایت در نظر گرفته می‌شود
    dist = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            dist[(i, j)] = INF

    # تعریف یک لیست برای نمایش تغییرات مجوزها
    changes = [(1, -1), (1, 1), (-1, -1), (-1, 1)]

    while not q.empty():
        curr_i, curr_j, curr_dist = q.get()

        # اگر به گره مقصد برسیم، آن را به عنوان جواب برمی‌گردانیم
        if curr_i == des_i and curr_j == des_j:
            return curr_dist

        # بررسی همسایه‌های گره فعلی و اضافه کردن آن‌ها به صف در صورت لازم
        for dx, dy in changes:
            next_i, next_j = curr_i + dx, curr_j + dy

            if is_valid(next_i, next_j, len(grid) - 1, len(grid[0]) - 1) and \
               grid[curr_i][curr_j][changes.index((dx, dy))] == '\\' and \
               grid[next_i][next_j][changes.index((-dx, -dy))] == '\\':

                if curr_dist + 1 < dist[(next_i, next_j)]:
                    dist[(next_i, next_j)] = curr_dist + 1
                    q.put((next_i, next_j, curr_dist + 1))

            elif is_valid(next_i, next_j, len(grid) - 1, len(grid[0]) - 1) and \
                    grid[curr_i][curr_j][changes.index((dx, dy))] == '/' and \
                    grid[next_i][next_j][changes.index((-dx, dy))] == '/':

                if curr_dist + 1 < dist[(next_i, next_j)]:
                    dist[(next_i, next_j)] = curr_dist + 1
                    q.put((next_i, next_j, curr_dist + 1))

    # اگر به گره مقصد نرسیدیم، باید -1 برگردانیم
    return -1


n, m = map(int, input().split())
start_i, start_j = map(int, input().split())
end_i, end_j = map(int, input().split())

# خواندن وضعیت اولیه‌ی مجوزها
grid = []
for i in range(n):
    row = input().strip()
    grid.append([row[j:j + 2] for j in range(0, len(row), 2)])

# فراخوانی تابع bfs و چاپ پاسخ
print(bfs(start_i, start_j, end_i, end_j, grid))
