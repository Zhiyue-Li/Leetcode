from collections import Counter
def firstUniqChar(self, s: str) -> int:
    counter = Counter(s)
    for x in counter.keys():
        if counter[x] == 1:
            return s.index(x)
    return -1