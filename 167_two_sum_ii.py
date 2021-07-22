# Approach 1: Same as two sum
def twoSum(self, numbers: list[int], target: int) -> list[int]:
    h = {}
    for i, num in enumerate(numbers, 1):
        n = target - num
        if n in h:
            return [h[n], i]
        else:
            h[num] = i

# Approach 2: Two pointers (Valid because list is sorted)
def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    s = numbers[left] + numbers[right]
    while s != target:
        if s < target:
            left += 1
        else:
            right -= 1
        s = numbers[left] + numbers[right]
    return [left + 1, right + 1]