def myAtoi(self, s):
    # remove left leading whitespaces
    s = s.lstrip()
    if not s:
        return 0
        
    positive = True
    res = '' 
        
        
    if s[0] == '-':
        positive = False
    elif s[0] == '+':
        positive = True
    elif not s[0].isdigit():
        return 0
    else:
        res += s[0]
            
    for i in range(1, len(s)):
        if not s[i].isdigit():
            break
        else:
            res += s[i]
    if res == "":
        return 0

    # Convert string to int
    res = int(res) if positive else -int(res)

    # Clamp
    limit = 2 ** 31
    if limit > res >= -limit:
        return res
    elif res  < -limit:
        return -limit
    else:
        return limit - 1