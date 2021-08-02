# Two pointers
def optimalUtilization(a, b, target):
    a = sorted(a, key=lambda x:x[1])
    b = sorted(b, key=lambda x:x[1])
    left = 0
    right = len(b) - 1
    min_diff = float('inf')
    res = []
    while left < len(a) and right >= 0:
        s = a[left][1] + b[right][1]
        diff = target - s
        if diff >= 0:
            if diff <= min_diff:
                if diff < min_diff:
                    res = []
                    min_diff = diff
                res.append([a[left][0], b[right][0]])
                right_start = right
                while right_start > 0 and b[right_start][1] == b[right_start-1][1]:
                    res.append([a[left][0], b[right_start-1][0]])
                    right_start -= 1
            left += 1
        else:
            right -= 1
    return res if res else [[]]


a = [[1, 5], [2, 5]]
b = [[1, 5], [2, 5], [3, 5]]
target = 10
print(optimalUtilization(a, b, target))