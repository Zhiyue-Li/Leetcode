from collections import defaultdict
def minWindow(self, s: str, t: str) -> str:
    if len(s) < len(t):
        return ""
    if s == "":
        return ""
    if t in s:
        return t
    remain = defaultdict(int)
    for c in t:
        remain[c] += 1
    missing = len(t)
    res_left = 0
    # this default value cannot be achieved
    res_right = len(s) + 1
    left = 0
    for right, c in enumerate(s, 1):
        # Current char is needed
        if remain[c] > 0:
            missing -= 1
        remain[c] -= 1
        # No char is missing
        if not missing:
            # Move left pointer if that char is not needed (negative)
            while remain[s[left]] < 0:
                remain[s[left]] += 1
                left += 1
            # Record current substring if shorter
            if right - left < res_right - res_left:
                # Return if current substring is minimum
                if right - left == len(t):
                    return s[left: right]
                res_left, res_right = left, right
            # Move left pointer after recording to look for other valid substring
            remain[s[left]] += 1
            left += 1
            missing += 1
        # if still missing char, move right pointer
    # if res_right is default value, return "" since not substring found
    return s[res_left: res_right] if res_right != len(s) + 1 else ""