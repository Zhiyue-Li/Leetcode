import heapq
def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
    # dic = {}
    # for p in points:
    #     dic[tuple(p)] = p[0] * p[0] + p[1] * p[1]
    # return heapq.nsmallest(k, dic.keys(), key=dic.get)
    points.sort(key=lambda p: p[0]*p[0]+p[1]*p[1])
    return points[:k]