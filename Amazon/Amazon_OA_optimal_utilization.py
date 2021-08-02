from heapq import heappop, heappush
def optimalUtilization(a, b, target):
    min_heap = []
    min_diff = float('inf')
    for index_a, val_a in a:
        for index_b, val_b in b:
            diff = target - val_a - val_b
            if diff >= 0 and diff <= min_diff:
                min_diff = diff
                while min_heap and min_heap[0][0] > diff:
                    heappop(min_heap)
                heappush(min_heap, (diff, [index_a, index_b]))
    res = []
    while min_heap:
        res.append(heappop(min_heap)[1])
    return res

a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
print(optimalUtilization(a, b, target))