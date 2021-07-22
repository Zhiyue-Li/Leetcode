def romanToInt(self, s: str) -> int:
    dic = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,            
        'X': 10,
        'V': 5,
        'I': 1
    }
    num = dic[s[-1]]
    for i in range(len(s) - 1, 0, -1):
        prev = dic[s[i - 1]]
        curr = dic[s[i]]
        num += (prev, -prev)[curr > prev]
    return num