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
    