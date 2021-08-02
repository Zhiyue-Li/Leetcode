from heapq import heappush, heappop
def treasureIsland(sea):
    row, col = len(sea)-1, len(sea[0])-1
    min_heap = [(0, (0, 0))]
    while min_heap:
        item = heappop(min_heap)
        step = item[0]
        posX, posY = item[1]
        for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
            newX, newY = posX+x, posY + y
            if 0 <= newX <= row and 0 <= newY <= col:
                if sea[newY][newX] == 'X':
                    return step + 1
                elif sea[newY][newX] == 'O':
                    sea[newY][newX] = 'D'
                    heappush(min_heap, (step+1, (newX, newY)))
    return -1

sea = [['O', 'O', 'O', 'O'],
       ['D', 'O', 'D', 'O'],
       ['O', 'O', 'O', 'O'],
       ['D', 'D', 'D', 'X']]

print(treasureIsland(sea))