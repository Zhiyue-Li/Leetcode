def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
    r = n % 14 if n % 14 != 0 else 14
    n = 0
    while n < r:
        c = cells.copy()
        for i in range(1, len(cells)-1):
            if c[i-1] == c[i+1] == 0 or c[i-1] == c[i+1] == 1:
                cells[i] = 1
            else:
                cells[i] = 0
        if n == 0:
            if cells[0] == 1:
                cells[0] = 0
            if cells[-1] == 1:
                cells[-1] = 0
        n += 1
    return cells