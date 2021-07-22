def reverse(self, x: int) -> int:
    sign = -1 if x < 0 else 1
    res = int(str(abs(x))[::-1]) * sign
    limit = 2 ** 31
    if  limit > res >= -limit:
        return res
    else:
        return 0