def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
    horizontalCuts.sort()
    verticalCuts.sort()
    horizontalCuts.insert(0, 0)
    horizontalCuts.append(h)
    verticalCuts.insert(0, 0)
    verticalCuts.append(w)
    h_diff = w_diff = 0
    for i in range(len(horizontalCuts) - 1):
        if horizontalCuts[i + 1] - horizontalCuts[i] > h_diff:
            h_diff = horizontalCuts[i + 1] - horizontalCuts[i]
    for i in range(len(verticalCuts) - 1):
        if verticalCuts[i + 1] - verticalCuts[i] > w_diff:
            w_diff = verticalCuts[i + 1] - verticalCuts[i]
    return (h_diff * w_diff) % (10 ** 9 + 7)