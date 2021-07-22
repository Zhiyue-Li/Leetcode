def generateParenthesis(self, n: int) -> list[str]:
    combinations = []
    def backTrack(res, left, right):
        if len(res) == n * 2:
            combinations.append(''.join(res))
            return
        if res.count('(') < n:
            res.append('(')
            backTrack(res, left+1, right)
            res.pop()
        if right < left:
            res.append(')')
            backTrack(res, left, right+1)
            res.pop()
    backTrack([], 0, 0)
    return combinations