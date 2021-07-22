from collections import Counter, defaultdict
import heapq
import re

def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    counts = Counter(re.split("[ !?',;.]", paragraph.lower()))
    if '' in counts:
        del counts['']
        
    counts = [(-count, word) for word, count in counts.items()]
    heapq.heapify(counts)
        
    while counts and counts[0][1] in banned:
        heapq.heappop(counts)
            
    return counts[0][1]

# Regex
def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    dic = defaultdict(int)
    words = re.findall(r'\w+', paragraph)
    count = 0
    res = ""
    for word in words :
        word = word.lower()
        if word not in banned : 
            dic[word] += 1
            if (dic[word] > count):
                count = dic[word]
                res = word
    return res