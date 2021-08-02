def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
    def backtrack(remain, combination, start):
        if remain == 0:
            res.append(combination.copy())
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            backtrack(remain-candidates[i], combination, i)
            combination.pop()
    res = []
    backtrack(target, [], 0)
    return res