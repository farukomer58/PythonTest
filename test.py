list = [4,5,5,5,5,3,2,9,2]
uniqueList = []

for number in list:
    if number not in uniqueList:
        uniqueList.append(number)
print(uniqueList)
