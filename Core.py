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
    
    #eliminating type 1 LAPs
    if len(LapType1s) != 0:
        for l in LapType1s:
            methods = findMethodDeclarations(sourceCodeDirectory)
            lines = createGetMethodComplement(sourceCodeDirectory, l.node)
            tempLines = copy.copy(lines)
            tempFirstLine = tempLines[0]
            temp = createGetMethodComplementName(lines[0], l, methods)
            firstLine = temp[0]
            lines[0] = firstLine
            insertMethodToTheEnd(sourceCodeDirectory, lines)
            createAndReplaceEditedFunction(sourceCodeDirectory, tempFirstLine, temp[1], l.node, tempLines)
            break
        continue
    
    #eliminating type 7 LAPs
    if len(LapType7s) != 0:
        for l in LapType7s:
            renameMethodInPlace(sourceCodeDirectory, l)
            break
        continue
    
    if deleteNotImplementedMethods:
    #eliminating type 5 LAPs
        if len(LapType5s) != 0:
            print('yeeeeesss')
            for l in LapType5s:
                removeMethodInPlace(sourceCodeDirectory, l)
                break
            continue

    if deleteNotImplementedMethods:
        if len(LapType1s) == 0 and len(LapType7s) == 0 and len(LapType5s) == 0:
            break
    else:
        if len(LapType1s) == 0 and len(LapType7s) == 0:
            break