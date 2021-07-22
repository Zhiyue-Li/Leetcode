# Approach 1: Store product from left and right in two lists
def productExceptSelf(self, nums: list[int]) -> list[int]:    
    x = 1
    n = nums.copy()
    for i in range(len(nums)):
        nums[i] = x
        x  *=  n[i]
    x = 1
    for i in range(len(nums)-1, -1, -1):
        nums[i] *= x
        x  *=  n[i]
    return nums

# Approach 2: Store product from left in list, track product from right using int
def productExceptSelf(self, nums: list[int]) -> list[int]:
    length = len(nums)
    answer = [0]*length
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]
    R = 1
    for i in reversed(range(length)):
        answer[i] = answer[i] * R
        R *= nums[i]
    return answer