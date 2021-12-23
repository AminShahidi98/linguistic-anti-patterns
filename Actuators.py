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

def createGetMethodComplementName(firstLine, lapObject, allMethodes):
    spaceSeen = False
    temp = ''
    parenthesesIndex = 0
    spaceSeenCounter = 0
    for i in range(0, len(firstLine)):
        if firstLine[i] == '(':
            parenthesesIndex = i
            break
        elif firstLine[i] == ' ':
            spaceSeen = True
            spaceSeenCounter += 1
        else:
            if spaceSeen:
                temp = firstLine[i]
                spaceSeen = False
                spaceSeenCounter = 0
            else:
                temp += firstLine[i]
    newNameBasic = 'complement_' + lapObject.node.name
    newName = newNameBasic
    newNameIndex = 2
    for i in allMethodes:
        if i.name == newName:
            newName = newNameBasic + '_' + str(newNameIndex)
            newNameIndex += 1
    firstLineComplement = firstLine[:parenthesesIndex-len(temp)-spaceSeenCounter] + newName + firstLine[parenthesesIndex:]
    newFunctionView = newName + '('
    for i in lapObject.node.parameters:
        newFunctionView += i.name
        newFunctionView += ', '
    newFunctionView = newFunctionView[:len(newFunctionView)-2]
    newFunctionView += ')'
    return (firstLineComplement, newFunctionView)

def createAndReplaceEditedFunction(sourceCodeDirectory, firstLine, newFunctionView, node, complementCodeList):
    newFunction = ''
    for i in firstLine:
        if i != '{':
            newFunction += i
        else:
            break
    newFunction = newFunction + '{\n' + 'return ' + newFunctionView + ';\n' +'}'
    fileLinesList = []
    with open(sourceCodeDirectory) as file:
        for line in file:
            fileLinesList.append(line.rstrip('\n')) #Append without disturbing extra blank lines of readline() method.
    for i in range(0, len(complementCodeList)):
        fileLinesList.pop(node.position.line-1)
    fileLinesList.insert(node.position.line-1, newFunction)
    result = "\n".join(fileLinesList[:])
    with open(sourceCodeDirectory, "w") as text_file:
        text_file.write(result)
