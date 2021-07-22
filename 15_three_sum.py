from collections import Counter

def threeSum(self, nums: list[int]) -> list[list[int]]:
    counter = Counter(nums)
    ans = set()
    if counter[0] >= 3:
        ans.add((0,0,0))
    nums = list(counter.keys())
    pos, neg = [x for x in nums if x > 0], [x for x in nums if x < 0]
    for a in pos:
        for b in neg:
            c = -(a + b)
            if c in counter and ((c != a and c != b) or counter[c] > 1):
                ans.add(tuple(sorted([a, b, c])))
    return ans