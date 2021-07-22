# Down to up
def trap(self, height: list[int]) -> int:
    if len(height) <= 1:
        return 0
    l = len(height)
    m = max(height)
    h = 0
    res = 0
    idx = [i for i in range(l) if height[i] > 0]
    if len(idx) == 1:
        return 0
    while h < m:
        for i in range(1, len(idx)):
            res += idx[i] - idx[i-1] - 1
        h += 1
        idx = [i for i in idx if height[i] > h]
        if len(idx) == 1:
            break
    return res

# Two pointers
def trap(self, height: list[int]) -> int:
    if len(height) < 2:
        return 0
    res = 0
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    while left < right:
        if left_max >= right_max:
            right -= 1
            if height[right] > right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
        else:
            left += 1
            if height[left] > left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
    return res

