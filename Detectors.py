from Utils import *
from Models import *
import javalang

def returnGetLAPType(node):
    if len(node.body) == 0:
        return Lap(5)
    elif len(node.body) == 1:
        if type(node.body[0]) == javalang.tree.ReturnStatement:
            pass
        else:
            return Lap(7)
    elif len(node.body) > 1:
        for i in node.body:
            if type(i) == javalang.tree.ReturnStatement:
                return(Lap(1))
        return Lap(7)
    return Lap(0)

def returnIsLAPType(node):
    flag = 0
    if len(node.body) == 0:
        return Lap(5)
    else:
        if node.return_type.name != 'boolean':
            return Lap(2)
        for i in node.body:
            if type(i) == javalang.tree.ReturnStatement:
                flag = 1
        if flag == 0:
            return Lap(8)
    return Lap(0)

def returnSetLAPType(node):
    if len(node.body) == 0:
        return Lap(5)
    for i in node.body:
        if type(i) == javalang.tree.ReturnStatement:
            return Lap(3)
    return Lap(0)

def returnIfType4LAP(node):
    lowerCasedName = separateStringToWords(node.name)[0].lower()
    keyNoun = lowerCasedName[len(lowerCasedName) - 1]
    if isPlural(keyNoun):
        print('is plural')
        return Lap(0)
    else:
        if keyNoun in singularDataTypes:
            if node.return_type.name in pluralDataTypes:
                return Lap(4)
            else:
                return Lap(0)
        else:
            if node.return_type.name in pluralDataTypes:
                return Lap(4)
            else:
                return Lap(0)

def returnIfType5LAP(node):
    if node.body == []:
        return Lap(5)
    else:
        return Lap(0)

def returnIfType12or14LAP(parentNode, node):
    nodeSplitedName = separateStringToWords(node.name)
    lastIndex = len(nodeSplitedName) - 1
    if isPlural(nodeSplitedName[lastIndex]):
        if parentNode.type.name in pluralDataTypes:
            return Lap(0)
        else:
            return Lap(14)
    elif not isPlural(nodeSplitedName[lastIndex]):
        if parentNode.type.name in pluralDataTypes:
            return Lap(12)
        else:
            return Lap(0)
    elif nodeSplitedName[lastIndex].lower() in ['list', 'array', 'set', 'tuple']:
        if parentNode.type.name in pluralDataTypes:
            return Lap(0)
        else:
            return Lap(14)
    else:
        return Lap(0)

def returnIfType13LAP(parentNode, node):
    nodeSplitedName = separateStringToWords(node.name)
    if nodeSplitedName[0] in booleanSugestions:
        if parentNode.type.name == 'boolean':
            return Lap(0)
        else:
            return Lap(13)
    else:
        return Lap(0)