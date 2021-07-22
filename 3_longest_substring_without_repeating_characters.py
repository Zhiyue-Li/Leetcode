# concise
def lengthOfLongestSubstring(self, s: str) -> int:
    dic = {}
    max_len = 0
    start = 0
    for i, c in enumerate(s):
        if c in dic:
            max_len = max(max_len, count)
            start = max(start, dic[c] + 1)
        count = i - start + 1
        dic[c] = i
    max_len = max(max_len, count)
    return max_len

# based on length
def lengthOfLongestSubstring(self, s: str) -> int:
    dic = {}
    max_len = count = start = 0
    for i, c in enumerate(s):
        # If duplicate char detected
        if c in dic:
            if max_len < count:
                max_len = count
            # Only change start if recorded position of duplicate char > start
            if dic[c] + 1 > start:
                start = dic[c] + 1
            # Calculate substring length
            count = i - start + 1
        else:
            count = i - start + 1
        # Store current char and position in dict
        dic[c] = i
    if max_len < count:
        max_len = count
    return max_len

# based on substring
def lengthOfLongestSubstring(self, s: str) -> int:
    if s == "":
        return 0
    sub = ""
    max_sub = ""
    for c in s:
        if c not in sub:
            sub += c
        else:
            if len(sub) > len(max_sub):
                max_sub = sub
            sub = sub.split(c)[1] + c
    if len(sub) > len(max_sub):
        max_sub = sub
    return len(max_sub)