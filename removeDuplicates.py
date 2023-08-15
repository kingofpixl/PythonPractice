numbers = [2,2,4,6,3,4,6,1]
goodList = []
for number in numbers:
    if number not in goodList:
        goodList.append(number)
print(goodList)