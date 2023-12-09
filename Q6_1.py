n = int(input())
heights = list(map(int, input().split()))

left, right = 0, n-1
max_left, max_right = 0, 0
water_volume = 0

while left <= right:
    if heights[left] < heights[right]:
        if heights[left] > max_left:
            max_left = heights[left]
        else:
            water_volume += max_left - heights[left]
        left += 1
    else:
        if heights[right] > max_right:
            max_right = heights[right]
        else:
            water_volume += max_right - heights[right]
        right -= 1

print(water_volume)
