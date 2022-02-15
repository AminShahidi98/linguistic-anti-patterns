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

def createMethodComplement(sourceCodeDirectory, getMethodNode):
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

def createMethodComplementName(firstLine, lapObject, allMethodes, isSetMethode):
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
    if isSetMethode:
        newNameBasic = lapObject.node.name + '_andLog'
    else:
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
    if len(lapObject.node.parameters) != 0:
        newFunctionView = newFunctionView[:len(newFunctionView)-2]
    newFunctionView += ')'
    #print(firstLineComplement)#fist line of complement function
    #print(newFunctionView)#the function call we put inside new function to call complement function
    return (firstLineComplement, newFunctionView)

def createAndReplaceEditedFunction(sourceCodeDirectory, firstLine, newFunctionView, node, complementCodeList, replaceReturnType):
    newFunction = ''
    for i in firstLine:
        if i != '{':
            newFunction += i
        else:
            break

    if replaceReturnType:
        if len(node.return_type.dimensions) != 0:
            newFunction = newFunction.replace(' ' + node.return_type.name + '[]', " boolean", 1)
            if node.return_type.name == 'int':
                newFunction = newFunction + '{\n' + '    int[] temp = ' + newFunctionView +';\n' + '    int size = temp.length;\n' + '    if (size == 0) {return false;}\n' + '    else if (size == 1){\n' + '        int tempInt = temp[0];\n' + "        if (tempInt == 0) {return false;}\n" + '        else {return true;}\n' + '    }\n' + '    else {return true;}\n    }'
            elif node.return_type.name == 'byte':
                newFunction = newFunction + '{\n' + '    byte[] temp = ' + newFunctionView +';\n' + '    int size = temp.length;\n' + '    if (size == 0) {return false;}\n' + '    else if (size == 1){\n' + '        byte tempByte = temp[0];\n' + "        if (tempByte == 0) {return false;}\n" + '        else {return true;}\n' + '    }\n' + '    else {return true;}\n    }'
            elif node.return_type.name == 'short':
                newFunction = newFunction + '{\n' + '    short[] temp = ' + newFunctionView +';\n' + '    int size = temp.length;\n' + '    if (size == 0) {return false;}\n' + '    else if (size == 1){\n' + '        short tempShort = temp[0];\n' + "        if (tempShort == 0) {return false;}\n" + '        else {return true;}\n' + '    }\n' + '    else {return true;}\n    }'
            elif node.return_type.name == 'long':
                newFunction = newFunction + '{\n' + '    long[] temp = ' + newFunctionView +';\n' + '    int size = temp.length;\n' + '    if (size == 0) {return false;}\n' + '    else if (size == 1){\n' + '        long tempLong = temp[0];\n' + "        if (tempLong == 0) {return false;}\n" + '        else {return true;}\n' + '    }\n' + '    else {return true;}\n    }'
            elif node.return_type.name == 'float':
                newFunction = newFunction + '{\n' + '    float[] temp = ' + newFunctionView +';\n' + '    int size = temp.length;\n' + '    if (size == 0) {return false;}\n' + '    else if (size == 1){\n' + '        float tempFloat = temp[0];\n' + "        if (tempFloat == 0) {return false;}\n" + '        else {return true;}\n' + '    }\n' + '    else {return true;}\n    }'
            elif node.return_type.name == 'double':
                newFunction = newFunction + '{\n' + '    double[] temp = ' + newFunctionView +';\n' + '    int size = temp.length;\n' + '    if (size == 0) {return false;}\n' + '    else if (size == 1){\n' + '        double tempDouble = temp[0];\n' + "        if (tempDouble == 0) {return false;}\n" + '        else {return true;}\n' + '    }\n' + '    else {return true;}\n    }'
            elif node.return_type.name == 'char':
                newFunction = newFunction + '{\n' + '    char[] temp = ' + newFunctionView +';\n' + '    int size = temp.length;\n' + '    if (size == 0) {return false;}\n' + '    else if (size == 1){\n' + '        char tempChar = temp[0];\n' + "        if (tempChar == '0' || tempChar == 'f' || tempChar == 'F') {return false;}\n" + '        else {return true;}\n' + '    }\n' + '    else {return true;}\n    }'
            elif node.return_type.name == 'String':
                newFunction = newFunction + '{\n' + '    String[] temp = ' + newFunctionView +';\n' + '    int size = temp.length;\n' + '    if (size == 0) {return false;}\n' + '    else if (size == 1){\n' + '        String tempString = temp[0].toLowerCase();\n' + '        if (tempString.equals("0") || tempString.equals("f") || tempString.equals("false")) {return false;}\n' + '        else {return true;}\n' + '    }\n' + '    else {return true;}\n    }'
            else:
                newFunction = newFunction + '{\n' + '    return ' + newFunctionView + ';\n' +'    }'

        else:
            newFunction = newFunction.replace(' ' + node.return_type.name, " boolean", 1)
            if node.return_type.name == 'int':
                newFunction = newFunction + '{\n' + '    int temp = ' + newFunctionView +';\n' + '    if (temp == 0) {return false;}\n    else {return true;}\n    }'
            elif node.return_type.name == 'byte':
                newFunction = newFunction + '{\n' + '    byte temp = ' + newFunctionView +';\n' + '    if (temp == 0) {return false;}\n    else {return true;}\n    }'
            elif node.return_type.name == 'short':
                newFunction = newFunction + '{\n' + '    short temp = ' + newFunctionView +';\n' + '    if (temp == 0) {return false;}\n    else {return true;}\n    }'
            elif node.return_type.name == 'long':
                newFunction = newFunction + '{\n' + '    long temp = ' + newFunctionView +';\n' + '    if (temp == 0) {return false;}\n    else {return true;}\n    }'
            elif node.return_type.name == 'float':
                newFunction = newFunction + '{\n' + '    float temp = ' + newFunctionView +';\n' + '    if (temp == 0) {return false;}\n    else {return true;}\n    }'
            elif node.return_type.name == 'double':
                newFunction = newFunction + '{\n' + '    double temp = ' + newFunctionView +';\n' + '    if (temp == 0) {return false;}\n    else {return true;}\n    }'
            elif node.return_type.name == 'char':
                newFunction = newFunction + "{\n" + "    char temp = " + newFunctionView +";\n" + "    if (temp == 'f' || temp == 'F' || temp == '0') {return false;}\n    else {return true;}\n    }"
            elif node.return_type.name == 'String':
                newFunction = newFunction + '{\n' + '    String temp = ' + newFunctionView +';\n' + '    temp = temp.toLowerCase();\n' + '    if (temp.equals("0") || temp.equals("f") || temp.equals("false") ) {return false;}\n    else {return true;}\n    }'
            else:
                newFunction = newFunction + '{\n' + '    return ' + newFunctionView + ';\n' +'    }'

    else: 
        newFunction = newFunction + '{\n' + '    return ' + newFunctionView + ';\n' +'    }'
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

def renameMethodInPlace(sourceCodeDirectory, lapObject, type4LAP):
    startLine = lapObject.node.position.line
    fileLinesList = []
    with open(sourceCodeDirectory) as file:
        for line in file:
            fileLinesList.append(line.rstrip('\n')) #Append without disturbing extra blank lines of readline() method.
    result = "\n".join(fileLinesList[:])
    if type4LAP:
        newMethodName = "calculateFor" + lapObject.node.name + '('
    else:
        newMethodName = "calculateFor" + lapObject.node.name + '('
    result = result.replace(lapObject.node.name + '(', newMethodName)
    with open(sourceCodeDirectory, "w") as text_file:
        text_file.write(result)

def removeMethodInPlace(sourceCodeDirectory, lapObject):
    startLine = lapObject.node.position.line
    startColumn = lapObject.node.position.column
    fileLinesList = []
    with open(sourceCodeDirectory) as file:
        for line in file:
            fileLinesList.append(line.rstrip('\n')) #Append without disturbing extra blank lines of readline() method.
    openCurlCount = 0
    closeCurlCount = 0
    firstLine = True
    endOfMethod = False
    newFileLinesList = []
    for l in fileLinesList[:startLine-1]:
        newFileLinesList.append(l)
    for line in fileLinesList[startLine-1:]:
        if endOfMethod:
            newFileLinesList.append(line)
            continue
        if firstLine:
            firstLine = False
            offset = []
            for i in range(0, startColumn):
                if line[i]=='{' or line[i]=='}':
                    offset.append(i)
            if len(offset) != 0:
                newLine = line[:max(offset)+1]
                newFileLinesList.append(newLine)
        if '{' not in line and '}' not in line:
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
                    newLine = line[charCount:]
                    newFileLinesList.append(newLine)
                    endOfMethod = True
                    break

    result = "\n".join(newFileLinesList[:])
    with open(sourceCodeDirectory, "w") as text_file:
        text_file.write(result)
        return 0

def resolveSetMethodeNameAndReturns(sourceCodeDirectory, node, methodeCodeList):
    usedModifiers = []
    for m in modifiers:
        if ' '+m+' ' in methodeCodeList[0]:
            usedModifiers.append(m)

    usedModifiersString = ''
    for m in usedModifiers:
        usedModifiersString += m + ' '

    variableNameBase = 'logFor_' + node.name
    variableName = variableNameBase
    index = 2
    #list of tuples. first member of each tuple is the name of the coresponding variable
    allGlobalVariables = returnVariableDeclarators(sourceCodeDirectory)[0]
    for v in allGlobalVariables:
        if variableName == v[0]:
            variableName = variableNameBase + '_' + str(index)
            index += 1
    
    variableLine = ''
    variableDataType = ''

    if len(node.return_type.dimensions) != 0:
        variableDataType = node.return_type.name + '[]'
    else:
        variableDataType = node.return_type.name
    
    variableLine = usedModifiersString + variableDataType + ' ' + variableName + ';'
    newFunctionAndVariable = ''
    
    newFunction = ''
    for i in methodeCodeList[0]:
        if i != '{':
            newFunction += i
        else:
            newFunction += ' {\n'
            break  

    if len(node.return_type.dimensions) != 0:
        newFunction = newFunction.replace(' ' + node.return_type.name + '[]',' void', 1)
    else:
       newFunction = newFunction.replace(' ' + node.return_type.name,' void', 1)
    

    newFunctionNameBase = node.name + '_WithLog'
    newFunctionName = newFunctionNameBase

    index = 2
    allMethods = findMethodDeclarations(sourceCodeDirectory)
    for m in allMethods:
        if newFunctionName == m.name:
            newFunctionName = newFunctionNameBase + '_' + str(index)
            index += 1

    newFunction = newFunction.replace(' ' + node.name, ' ' + newFunctionName, 1)

    for line in methodeCodeList[1:]:
        newFunction = newFunction + line + '\n'

    newFunctionAndVariable = '    ' + variableLine + '\n' + newFunction
    newFunctionAndVariableList = newFunctionAndVariable.split('\n')
    for i in range(0, len(newFunctionAndVariableList)):
        if 'return' in newFunctionAndVariableList[i]:
            newFunctionAndVariableList[i] = newFunctionAndVariableList[i].replace('return', ' ' + variableName + ' = ', 1)
    newFunctionAndVariable = "\n".join(newFunctionAndVariableList[:])

    fileLinesList = []
    with open(sourceCodeDirectory) as file:
        for line in file:
            fileLinesList.append(line.rstrip('\n')) #Append without disturbing extra blank lines of readline() method.
    for i in range(0, len(methodeCodeList)):
        fileLinesList.pop(node.position.line-1)
    fileLinesList.insert(node.position.line-1, newFunctionAndVariable)
    result = "\n".join(fileLinesList[:])
    with open(sourceCodeDirectory, "w") as text_file:
        text_file.write(result)