from collections import defaultdict
def transactionLogs(logData, threshold):
    logData = [x[0].split() for x in logData]
    dic = defaultdict(int)
    res = set()
    for log in logData:
        if log[0] != log[1]:
            dic[log[1]] += 1
            if dic[log[1]] == threshold:
                res.add(log[1])
        dic[log[0]] += 1
        if dic[log[0]] == threshold:
            res.add(log[0])
    return list(res)

logData = [['345366 89921 45'],
           ['029323 38239 23'],
           ['38239 345366 15'],
           ['029323 38239 77'],
           ['345366 38239 23'],
           ['029323 345366 13']]
threshold = 3
print(transactionLogs(logData, threshold))