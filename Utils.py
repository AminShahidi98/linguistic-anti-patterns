import javalang
from Models import GetMethodLAP

def tokenize(sourceCodeDirectory):
    sourceCode = open(sourceCodeDirectory, 'r').read()
    tokensList = list(javalang.tokenizer.tokenize(sourceCode))
    return tokensList

def parse(sourceCodeDirectory):
    sourceCode = open(sourceCodeDirectory, 'r').read()
    tree = javalang.parse.parse(sourceCode)
    return tree

def findMethodDeclarations(sourceCodeDirectory):
    methodDeclarations = []
    tree = parse(sourceCodeDirectory)
    for path, node in tree.filter(javalang.tree.MethodDeclaration):
        methodDeclarations.append(node)
    return methodDeclarations

'''
test = findMethodDeclarations("Demo.java")
for t in test:
    tt = GetMethodLAP(t, "test123", "nothing right now")
    print(tt)
'''