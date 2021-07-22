from collections import defaultdict, Counter
import heapq
# Approach 1: O(N log N) using sort
def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    dic = defaultdict(int)
    for i in nums:
        dic[i] += 1
    # counter = Counter(nums)
    return [x[0] for x in sorted(dic.items(), key=lambda t:-t[1])[:k]]

# Approach 2: O(N log k) using heap
def topKFrequent(self, nums: list[int], k: int) -> list[int]: 
    # O(1) time 
    if k == len(nums):
        return nums
    # 1. build hash map : character and how often it appears
    # O(N) time
    count = Counter(nums)   
    # 2-3. build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    return heapq.nlargest(k, count.keys(), key=count.get)