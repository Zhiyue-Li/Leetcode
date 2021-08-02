from collections import defaultdict
def countComponents(self, n: int, edges: list[list[int]]) -> int:
    def dfs(key, dic, visited):
        visited.add(key)
        for value in dic[key]:
            if value not in visited:
                dfs(value, dic, visited)
                
    dic = defaultdict(list)
    for first, second in edges:
        dic[first].append(second)
        dic[second].append(first)

    res = 0
    visited = set()
    for key in dic.keys():
        if key not in visited:
            dfs(key, dic, visited)
            res += 1
    res += (n - len(visited))
    return res