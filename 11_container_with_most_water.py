def maxArea(self, height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    max_h = max(height)
    while (right - left) * max_h >= max_area:
        area = (right-left) * min(height[left], height[right])
        if area > max_area:
            max_area = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area