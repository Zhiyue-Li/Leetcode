def numberToWords(self, num: int) -> str:
    def threeDigit(n):
        s = ""
        h = n // 100
        td = n % 100
        t = td // 10
        d = td % 10
        if h > 0:
            s += dic[h] + ' Hundred '
        if t >= 2:
            s += dic[t*10]
            if d > 0 and d < 10:
                s += ' ' + dic[d]
        elif td > 9 and td < 20:
            s += dic[td]
        elif td <= 9 and td > 0:
            s += dic[d]
        return s

    dic = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
        9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
        16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty',
        40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }
        
    if num == 0:
        return "Zero"
    l = []
    res = ""
    while num > 999:
        l.append(num % 1000)
        num //= 1000
    l.append(num % 1000)

    for i in range(len(l)):
        res = threeDigit(l[i]) + res
        if i != len(l) - 1:
            if i % 3 == 0:
                res = ' Thousand ' + res
            elif i % 3 == 1:
                res = ' Million ' + res
            else:
                res = ' Billion ' + res
    res = res.replace('  ', ' ').replace('Million Thousand', 'Million')
    res = res.replace('Billion Million', 'Billion')
    return res.strip(' ')

def numberToWords(self, num):
    """
    :type num: int
    :rtype: str
    """
    def one(num):
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return switcher.get(num)

    def two_less_20(num):
        switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switcher.get(num)
        
    def ten(num):
        switcher = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switcher.get(num)
        

    def two(num):
        if not num:
            return ''
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            tenner = num // 10
            rest = num - tenner * 10
            return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)
        
    def three(num):
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return one(hundred) + ' Hundred ' + two(rest) 
        elif not hundred and rest: 
            return two(rest)
        elif hundred and not rest:
            return one(hundred) + ' Hundred'
        
    billion = num // 1000000000
    million = (num - billion * 1000000000) // 1000000
    thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
    if not num:
        return 'Zero'
        
    result = ''
    if billion:        
        result = three(billion) + ' Billion'
    if million:
        result += ' ' if result else ''    
        result += three(million) + ' Million'
    if thousand:
        result += ' ' if result else ''
        result += three(thousand) + ' Thousand'
    if rest:
        result += ' ' if result else ''
        result += three(rest)
    return result