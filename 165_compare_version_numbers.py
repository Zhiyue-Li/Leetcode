def compareVersion(self, version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    if len(v1) > len(v2):
        v2 += [0] * (len(v1) - len(v2))
    else:
        v1 += [0] * (len(v2) - len(v1))
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return 1
        elif v1[i] < v2[i]:
            return -1
    return 0

def compareVersion(self, version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    i = j = 0
    while i < len(v1) and j < len(v2):
        if v1[i] > v2[j]:
            return 1
        elif v1[i] < v2[j]:
            return -1
        i += 1
        j += 1
    while i < len(v1):
        if v1[i] > 0:
            return 1
        i += 1
    while j < len(v2):
        if v2[j] > 0:
            return -1
        j += 1
    return 0