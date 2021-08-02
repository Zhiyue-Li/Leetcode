from collections import defaultdict
def largestItemAssociation(itemAssociation):
    dic = defaultdict(list)
    for first, second in itemAssociation:
        dic[first].append(second)
        dic[second].append(first)

    res = []
    visited = set()
    for key in dic.keys():
        if key not in visited:
            chain = []
            dfs(key, chain, dic, visited)
            if len(chain) > len(res):
                res = chain
    return res

def dfs(key, chain, dic, visited):
    chain.append(key)
    visited.add(key)
    for value in dic[key]:
        if value not in visited:
            dfs(value, chain, dic, visited)

itemAssociation = [['Item1', 'Item2'],
                   ['Item3', 'Item4'],
                   ['Item4', 'Item5'],
                   ['Item3', 'Item6'],
                   ['Item6', 'Item7'],
                   ['Item7', 'Item8']]
print(largestItemAssociation(itemAssociation))