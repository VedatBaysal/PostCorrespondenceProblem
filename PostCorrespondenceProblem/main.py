import PostCorrespondenceProblem
start = True
while (start == True):
    try:
        maxSizeOfQueue = int(input("Enter Max size of queue: "))
        maxTotalNumOfStates = int(input("Enter  Max total number of states: "))
        inputFlag = int(input("Enter Either 0 or 1 (refers to (*) input in Input section): "))
        totalNumDominoues = int(input("Enter the number of Dominoes: "))
        dominoes = []
        print("Dominoes (Please Enter one by one)")
        print("-------------------------\n")

        for i in range(totalNumDominoues):
            top = input("Top Domino: ")
            bottom = input("Bottom Domino: ")
            dominoes.append([top,bottom])
        postCorrespondenceProblem = PostCorrespondenceProblem.PostCorrespondenceProblem(maxSizeOfQueue,maxTotalNumOfStates,inputFlag,totalNumDominoues,dominoes)
        print("\n")
        result = postCorrespondenceProblem.solve()
        print("\n")
        print(result)
        start = False

    except:
        print("Unexpected Error (Please Control Your Inputs) \n")
        start = True;
