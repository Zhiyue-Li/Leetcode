def threeSumClosest(self, nums: list[int], target: int) -> int:
    # Sort the list to use two pointer
    nums.sort()
    diff = float('inf')
    # Return if list length = 3
    if len(nums) == 3:
        return sum(nums)
    for i in range(len(nums)):
        # Skip if current element = previous element (duplicated)
        if i and nums[i] == nums[i-1]:
            continue
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if abs(diff) > abs(target - s):
                diff = target - s
            if s > target:
                hi -= 1
            elif s < target:
                lo += 1
            else:
                return s
    return target - diff