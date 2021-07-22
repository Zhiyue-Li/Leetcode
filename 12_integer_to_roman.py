def intToRoman(self, num: int) -> str:
    r = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),            
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    res = ''
    for c in r:
        c0 = c[0]
        while num >= c0:
            num = num - c0
            res += c[1]
            if num == 0:
                break
        if num == 0:
            break
        
    return res

def intToRoman(self, num: int) -> str:

    def cal(n, t, f, o):
        res = ""
        if n > 0 and n < 4:
            res = o * n
        elif n >= 4 and n <= 5:
            res = (5-n) * o + f
        elif n > 5 and n <=8:
            res = f + (n-5) * o
        elif n == 9:
            res = o + t
        return res
        
    thou = num // 1000
    remain = num % 1000
    hun = remain // 100
    remain = remain % 100
    ten = remain // 10
    remain = remain % 10

    thou_rom = "M" * thou
    hun_rom = cal(hun, "M", "D", "C")
    ten_rom = cal(ten, "C", "L", "X")
    dig = cal(remain, "X", "V", "I")
    return thou_rom + hun_rom + ten_rom + dig