def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
        
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
        
    for left, right in intervals[1:]:
        if left > res[-1][1]:
            res.append([left, right])
        else:
            if right > res[-1][1]:
                res[-1][1] = right
    return res