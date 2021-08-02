# Two pointer
def freshPromotion(codeList, shoppingCart):
    cartPointer = 0
    codeIndex = 0
    while codeIndex < len(codeList):
        codePointer = 0
        while codePointer < len(codeList[codeIndex]) and cartPointer < len(shoppingCart):
            if codeList[codeIndex][codePointer] == shoppingCart[cartPointer] or codeList[codeIndex][codePointer] == 'anything':
                codePointer += 1
            else:
                codePointer = 0
            cartPointer += 1
        if codePointer != len(codeList[codeIndex]):
            return False
        codeIndex += 1
    return codeIndex == len(codeList)
        
            
            
codeList = [['banana', 'anything'], ['banana', 'banana', 'anything']]
shoppingCart = ['banana', 'orange', 'banana', 'apple', 'apple']
print(freshPromotion(codeList, shoppingCart))