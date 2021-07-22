def strStr(self, haystack: str, needle: str) -> int:
    i = 0
    if haystack == needle:
        return 0
    # While remaining length of haystack is larger than needle length
    while (i + len(needle)) <= len(haystack):
        # Compare the current substring with needle
        if haystack[i : i + len(needle)] == needle:
            return i
        i += 1
    return -1