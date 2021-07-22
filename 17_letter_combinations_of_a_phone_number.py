def letterCombinations(self, digits: str) -> list[str]:
    if len(digits) == 0: 
        return []
        
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def backTrack(index, res):
        if index == len(digits):
            combinations.append(''.join(res))
            return
        for letter in letters[digits[index]]:
            res.append(letter)
            backTrack(index+1, res)
            res.pop()
        
    combinations = []
    backTrack(0, [])
    return combinations