from Utils import *

def insertMethodToTheEnd(sourceCodeDirectory, methodCodeLinesList):
    fileLinesList = []
    with open(sourceCodeDirectory) as file:
        for line in file:
            fileLinesList.append(line.rstrip('\n')) #Append without disturbing extra blank lines of readline() method.
    fileLinesList[len(fileLinesList)-1] = fileLinesList[len(fileLinesList)-1][:len(fileLinesList[len(fileLinesList)-1])-1] #Removed the } at the end of file.
    for line in methodCodeLinesList:
        fileLinesList.append(line)
    fileLinesList.append('}')
    result = "\n".join(fileLinesList[:])
    with open(sourceCodeDirectory, "w") as text_file:
        text_file.write(result)

def createGetMethodComplement(sourceCodeDirectory, getMethodNode):
    startLine = getMethodNode.position.line
    startColumn = getMethodNode.position.column
    fileLinesList = []
    with open(sourceCodeDirectory) as file:
        for line in file:
            fileLinesList.append(line.rstrip('\n')) #Append without disturbing extra blank lines of readline() method.
    openCurlCount = 0
    closeCurlCount = 0
    complementCodeList = []
    isFirstline = True
    for line in fileLinesList[startLine-1:]:
        if isFirstline:
            isFirstline = False
            offset = []
            for i in range(0, startColumn):
                if line[i]=='{' or line[i]=='}':
                    offset.append(i)
            if len(offset) != 0:
                line = line[max(offset)+1:]
        if '{' not in line and '}' not in line:
            complementCodeList.append(line)
            continue
        else:     
            charCount = 0
            for c in line:
                charCount += 1
                if c == '{':
                    openCurlCount += 1
                elif c == '}':
                    closeCurlCount += 1
                if openCurlCount!=0 and closeCurlCount!=0 and openCurlCount==closeCurlCount:
                    complementCodeList.append(line[:charCount])
                    return complementCodeList
            complementCodeList.append(line)