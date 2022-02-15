from javalang.tree import MethodDeclaration
from Utils import *
from Detectors import *
from Actuators import *
from Models import *
import copy

while True:
    deleteNotImplementedMethods = str(input("Remove Not implemented methods too?(y/n): "))
    if deleteNotImplementedMethods == 'y' or deleteNotImplementedMethods == 'n':
        break
    else:
        print("((INCORRECT INPUT))")

if deleteNotImplementedMethods == 'y':
    deleteNotImplementedMethods = True
else:
    deleteNotImplementedMethods = False
#we will stay at this loop till all the LAPs are eliminated.
countFlag = 0
while True:
    sourceCodeDirectory = 'Demo.java'
    methods = findMethodDeclarations(sourceCodeDirectory)
    getMethods = []
    setMethods = []
    isMethods = []
    for m in methods:
        if returnGetMethodSmell(m) == 'getMethod':
            getMethods.append(m)
        if returnSetMethodSmell(m) == 'setMethod':
            setMethods.append(m)
        if returnIsMethodSmell(m) == 'isMethod':
            isMethods.append(m)

    LapType1s = []
    LapType2s = []
    LapType3s = []
    LapType4s = []
    LapType5s = []
    LapType7s = []
    LapType8s = []
    LapType12s = []
    LapType13s = []
    LapType14s = []

    allVariables = returnVariableDeclarators(sourceCodeDirectory)
    globalVariables = allVariables[0]
    localVariables = allVariables[1]


    #In this section we create LAP objects out of node objects having LAP.
    #Store same LAPs in same lists. Lists are up.
    for gm in getMethods:
        if returnGetLAPType(gm) == Lap(1):
            newLap = GetMethodLAP(gm, Lap(1), '"Get" more than accessor', 1)
            LapType1s.append(newLap)
        elif returnGetLAPType(gm) == Lap(5):
            newLap = GetMethodLAP(gm, Lap(5), 'Not implemented condition', 1)
            LapType5s.append(newLap)
        elif returnGetLAPType(gm) == Lap(7):
            newLap = GetMethodLAP(gm, Lap(7), 'Get methode does not return', 1)
            LapType7s.append(newLap)

    for im in isMethods:
        if returnIsLAPType(im) == Lap(2):
            newLap = IsMethodLAP(im, Lap(2), 'Is returns more than a boolean', 1)
            LapType2s.append(newLap)
        elif returnIsLAPType(im) == Lap(5):
            newLap = IsMethodLAP(im, Lap(5), 'Not implemented condition', 1)
            LapType5s.append(newLap)
        elif returnIsLAPType(im) == Lap(8):
            newLap = IsMethodLAP(im, Lap(8), 'Not answered question', 1)
            LapType8s.append(newLap)

    for sm in setMethods:
        if returnSetLAPType(sm) == Lap(3):
            newLap = SetMethodLAP(sm, Lap(3), 'Set methode returns', 1)
            LapType3s.append(newLap)
        elif returnSetLAPType(sm) == Lap(5):
            newLap = SetMethodLAP(sm, Lap(5), 'Not implemented condition', 1)
            LapType5s.append(newLap)


    if countFlag == 0:
        countFlag = 1
        if deleteNotImplementedMethods:
            LAPsCount = len(LapType1s) + len(LapType7s) + len(LapType2s) + len(LapType3s)  + len(LapType5s)
            print("\n")
            print("total Number of linguistic antipatterns found: " + str(LAPsCount))
            print("\n")
            print("------------------------------------------------")
            print("Anti-pattern name                         | Count")
            print("------------------------------------------------")
            print('"Get" more than an accessor:              | ' + str(len(LapType1s)))
            print('Get method does not return:               | ' + str(len(LapType7s)))
            print('Is returns more than a boolean:           | ' + str(len(LapType2s)))
            print('Set method returns:                       | ' + str(len(LapType3s)))
            print('Not implemented method:                   | ' + str(len(LapType5s)))

        else:
            LAPsCount = len(LapType1s) + len(LapType7s) + len(LapType2s) + len(LapType3s)
            print("\n")
            print("total Number of linguistic antipatterns found: " + str(LAPsCount))
            print("\n")
            print("------------------------------------------------")
            print("Anti-pattern name                         | Count")
            print("------------------------------------------------")
            print('"Get" more than an accessor:              | ' + str(len(LapType1s)))
            print('Get method does not return:               | ' + str(len(LapType7s)))
            print('Is returns more than a boolean:           | ' + str(len(LapType2s)))
            print('Set method returns:                       | ' + str(len(LapType3s)))

    #eliminating type 1 LAPs
    if len(LapType1s) != 0:
        for l in LapType1s:
            methods = findMethodDeclarations(sourceCodeDirectory)
            lines = createMethodComplement(sourceCodeDirectory, l.node)
            tempLines = copy.copy(lines)
            tempFirstLine = tempLines[0]
            temp = createMethodComplementName(lines[0], l, methods, False)
            firstLine = temp[0]
            lines[0] = firstLine
            insertMethodToTheEnd(sourceCodeDirectory, lines)
            createAndReplaceEditedFunction(sourceCodeDirectory, tempFirstLine, temp[1], l.node, tempLines, False)
            break
        continue
    
    #eliminating type 7 LAPs
    if len(LapType7s) != 0:
        for l in LapType7s:
            renameMethodInPlace(sourceCodeDirectory, l, False)
            break
        continue
    
    if deleteNotImplementedMethods:
    #eliminating type 5 LAPs
        if len(LapType5s) != 0:
            for l in LapType5s:
                removeMethodInPlace(sourceCodeDirectory, l)
                break
            continue
    
    #eliminating type 2 LAPs
    if len(LapType2s) != 0:
        for l in LapType2s:
            methods = findMethodDeclarations(sourceCodeDirectory)
            lines = createMethodComplement(sourceCodeDirectory, l.node)
            tempLines = copy.copy(lines)
            tempFirstLine = tempLines[0]
            temp = createMethodComplementName(lines[0], l, methods, False)
            firstLine = temp[0]
            lines[0] = firstLine
            insertMethodToTheEnd(sourceCodeDirectory, lines)
            createAndReplaceEditedFunction(sourceCodeDirectory, tempFirstLine, temp[1], l.node, tempLines, True)
            break
        continue   

    #eliminating type 3 LAPs
    if len(LapType3s) != 0:
        for l in LapType3s:
            methods = findMethodDeclarations(sourceCodeDirectory)
            lines = createMethodComplement(sourceCodeDirectory, l.node)
            resolveSetMethodeNameAndReturns(sourceCodeDirectory, l.node, lines)
            break
        continue


    if deleteNotImplementedMethods:
        if len(LapType1s) == 0 and len(LapType7s) == 0 and len(LapType2s) == 0 and len(LapType3s) == 0 and len(LapType5s) == 0:
            break
    else:
        if len(LapType1s) == 0 and len(LapType7s) == 0 and len(LapType2s) == 0 and len(LapType3s) == 0:
            break