def twoSum(nums: list[int], target: int) -> list[int]:
    # Use dict to store traversed elements
    h = {}
    for i, num in enumerate(nums):
        # Number to find
        n = target - num
        # Return if number exist in dict
        if n in h:
            return [h[n], i]
        # Else store current element in dict
        else:
            h[num] = i