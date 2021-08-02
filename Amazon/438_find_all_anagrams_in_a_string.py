from collections import Counter
# Approach 1: Using counter
def findAnagrams(self, s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    res = []
    target = Counter(p)
    counter = Counter()
    for i in range(len(s)):
        counter[s[i]] += 1
        if i >= len(p):
            if counter[s[i - len(p)]] == 1:
                del counter[s[i - len(p)]]
            else:
                counter[s[i - len(p)]] -= 1
        if counter == target:
            res.append(i - len(p) + 1)
    return res

# Approach 2: Using hash value
def findAnagrams(self, s: str, p: str) -> list[int]:
    LS, LP, S, P, A = len(s), len(p), 0, 0, []
    if LP > LS: return []
    for i in range(LP): 
        S, P = S + hash(s[i]), P + hash(p[i])
            
    if S == P: A.append(0)
    for i in range(LP, LS):
        S += hash(s[i]) - hash(s[i-LP])
        if S == P: A.append(i-LP+1)
    return A