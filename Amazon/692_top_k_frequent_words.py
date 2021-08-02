from collections import defaultdict
from heapq import heappop, heappush
# Define a class to help comparison between objects
class Item:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count

# Using counter & heap
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        h = []
        for w, c in counter.items():
            item = Item(c, w)
            if len(h) < k:
                heappush(h, item)
            elif item > h[0]:
                heappop(h)
                heappush(h, item)
        res = []
        while(h):
            res.append(heappop(h).word)
        return res[::-1] 