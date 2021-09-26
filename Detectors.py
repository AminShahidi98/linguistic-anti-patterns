from Utils import *
from Models import *
import javalang

def returnGetLAPType(node):
    if len(node.body) == 0:
        return Lap(7)
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

test = findMethodDeclarations("Demo.java")
for t in test:
    if returnGetMethodSmell(t)=='getMethod' or returnGetMethodSmell(t)=='maybeGetMethod':
        print(returnGetLAPType(t))
        print("****************************")