from Utils import *
from Models import *
import javalang

def returnGetLAPType(node):
    if node.body == None:
        #It's an abstract method.
        return Lap(0)
    if len(node.body) == 0:
        return Lap(5)
    if node.return_type.name == 'void':
        return Lap(7)
    if len(node.body) > 1:
        return Lap(1)
    elif len(node.body) == 1:
        if str(type(node.body[0])) == "<class 'javalang.tree.IfStatement'>":
            return Lap(1)
        else:
            return Lap(0)
    return Lap(0)

def returnIsLAPType(node):
    if node.body == None:
        #It's an abstract method.
        return Lap(0)
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
    if node.body == None:
        #It's an abstract method.
        return Lap(0)
    if len(node.body) == 0:
        return Lap(5)
    if node.return_type.name != 'void':
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
            if len(node.return_type.dimensions) != 0:
                return Lap(4)
            else:
                return Lap(0)
        else:
            if len(node.return_type.dimensions) != 0:
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
        if len(parentNode.type.dimensions)!=0:
            return Lap(0)
        else:
            return Lap(14)
    elif not isPlural(nodeSplitedName[lastIndex]):
        if len(parentNode.type.dimensions)!=0:
            return Lap(12)
        else:
            return Lap(0)
    elif nodeSplitedName[lastIndex].lower() in ['list', 'array', 'set', 'tuple']:
        if len(parentNode.type.dimensions)!=0:
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