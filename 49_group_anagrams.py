def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    dic = {}
    for s in strs:
        sort_s = tuple(sorted(s))
        if sort_s in dic:
            dic[sort_s].append(s)
        else:
            dic[sort_s] = [s]
    return dic.values()