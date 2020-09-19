class PostCorrespondenceProblem():
    def __init__(self, maxSizeOfQueue, maxTotalNumOfStates, inputFlag, totalNumDominoues, dominoes):
        self.maxSizeOfQueue = maxSizeOfQueue
        self.maxTotalNumOfStates = maxTotalNumOfStates
        self.inputFlag = inputFlag
        self.totalNumDominoues = totalNumDominoues
        self.dominoes = dominoes
    def solve(self):
        tempTop = ""
        tempBottom = ""
        topSide = ""
        bottomSide = ""
        temp = ""
        isStart = False
        isFinish = False
        isTopSideLong = False
        for i in range(self.totalNumDominoues):
            if(isFinish == True):
                break
            tempTop = self.dominoes[i][0]
            tempBottom = self.dominoes[i][1]
            if(len(tempTop) < len(tempBottom)):
                if(tempTop == tempBottom[0:len(tempTop)]):
                    isStart = True
                    topSide = tempTop
                    bottomSide = tempBottom
                else:
                        isStart = False
            else:
                if(tempBottom == tempTop[0:len(tempBottom)]):
                    isStart = True
                    topSide = tempTop
                    bottomSide = tempBottom
            if(isStart == True):
                     lastAddedIndex = -1
                     repeatCount = 0;
                     for j in range(self.totalNumDominoues):
                         result = PostCorrespondenceProblem.nextStep(self,topSide,bottomSide)
                         if(result[0] != topSide and result[1] != bottomSide):
                             if(lastAddedIndex == result[2]):
                                 if(repeatCount > self.inputFlag):
                                     isFinish = True
                                     break
                             else:
                                lastAddedIndex = result[2]
                             topSide = result[0]
                             bottomSide = result[1]
                             if(topSide != "" and topSide == bottomSide):
                                 isFinish = True
                                 break
                         else:
                             topSide = ""
                             bottomSide = ""
                             isStart = False
                             break
        if (topSide != "" and topSide == bottomSide):
            return bottomSide
        return False

    def nextStep(self,topSide,bottomSide):
        lastAddedIndex = -2
        isNextStep = False
        tempTop = ""
        tempBottom = ""
        isTopSideTempLong = False
        if(len(topSide) > len(bottomSide)):
            leftCharCount = len(topSide) - len(bottomSide)
            temp = topSide[-leftCharCount:]
            isTopSideLong = True
        else:
            leftCharCount = len(bottomSide) - len(topSide)
            temp = bottomSide[-leftCharCount:]
            isTopSideLong = False
        for i in range(self.totalNumDominoues):
            if(isTopSideLong == True):
                if(temp == self.dominoes[i][1][0:leftCharCount]):
                    lastAddedIndex = i
                    tempTop = topSide + self.dominoes[i][0]
                    tempBottom = bottomSide + self.dominoes[i][1]
            else: 
                if(temp == self.dominoes[i][0][0:leftCharCount]):
                    lastAddedIndex = i
                    tempTop = topSide + self.dominoes[i][0]
                    tempBottom = bottomSide + self.dominoes[i][1]
            if(tempTop !="" and tempBottom !="" and (tempTop == tempBottom[0:len(tempTop)] or tempBottom == tempTop[0:len(tempBottom)])):
                if(tempTop != tempBottom ):
                    if(len(tempTop) > len(tempBottom)):
                        leftCharCount = len(tempTop) - len(tempBottom)
                        temp = tempTop[-leftCharCount:]
                        isTopSideTempLong = True
                    else:
                        leftCharCount = len(tempBottom) - len(tempTop)
                        temp = tempBottom[-leftCharCount:]
                        isTopSideTempLong = False
                if (isTopSideTempLong == True):
                    for j in range(self.totalNumDominoues):
                        if(temp == self.dominoes[j][1][0:leftCharCount]):
                            isNextStep = True
                            break
                        else: 
                            isNextStep = False
                else:
                    for j in range(self.totalNumDominoues):
                        if(temp == self.dominoes[j][0][0:leftCharCount]):
                            isNextStep = True
                            break
                        else: 
                            isNextStep = False
                if(isNextStep == True):
                    topSide = tempTop
                    bottomSide = tempBottom
                else:
                    tempTop = topSide
                    tempBottom = bottomSide
        return [topSide,bottomSide,lastAddedIndex]