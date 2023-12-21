finalList = ['']
inputList = "cheese, tomatoes, mushrooms, egg, ham, onions, anchovies, peppers"
i = 0
for character in inputList:
    if (character!=","):
        finalList[i]+=character
    else:
        finalList.append("")
        i+=1
print(finalList)
for i in range(len(finalList)):
    finalList[i] = finalList[i].upper()
    i+=1
print(finalList)