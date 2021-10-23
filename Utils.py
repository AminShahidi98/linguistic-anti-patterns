from Models import *
import javalang
from wordsegment import segment, load
load()
import inflect
inflect = inflect.engine()

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
        if node.return_type == None:
            void = customReturnType('void')
            node.return_type = void
        methodDeclarations.append(node)
    return methodDeclarations

def separateStringToWords(string):
    return segment(string)

def returnGetMethodSmell(node):
    lowerCasedName = separateStringToWords(node.name)[0].lower()
    if len(lowerCasedName) < 3:
        return 'notGetMethod'
    if lowerCasedName == 'get':
        return 'getMethod'
    elif lowerCasedName[0:3] == 'get':
        return 'maybeGetMethod'
    else:
        return 'notGetMethod'

def returnIsMethodSmell(node):
    lowerCasedName = separateStringToWords(node.name)[0].lower()
    if len(lowerCasedName) < 2:
        return 'notIsMethod'
    if lowerCasedName == 'is':
        return 'isMethod'
    elif lowerCasedName[0:2] == 'is':
        return 'maybeIsMethod'
    else:
        return 'notIsMethod'

def returnSetMethodSmell(node):
    lowerCasedName = separateStringToWords(node.name)[0].lower()
    if len(lowerCasedName) < 3:
        return 'notSetMethod'
    if lowerCasedName == 'set':
        return 'setMethod'
    elif lowerCasedName[0:3] == 'set':
        return 'maybeSetMethod'
    else:
        return 'notSetMethod'

def isPlural(word):
    if inflect.singular_noun(word) == False:
        return False
    else:
        return True

def returnVariableDeclarators(sourceCodeDirectory):
    globalVariablesList = []
    localVariablesList = []
    tree = parse(sourceCodeDirectory)
    for path, node in tree.filter(javalang.tree.FieldDeclaration):
        for p,  v in node.filter(javalang.tree.VariableDeclarator):
            globalVariablesList.append((v.name, node.position.line, node.type.name, 'global'))
    
    tree = parse(sourceCodeDirectory)
    for path, node in tree.filter(javalang.tree.LocalVariableDeclaration):
        for p, v in node.filter(javalang.tree.VariableDeclarator):
            localVariablesList.append((v.name, node.position.line, node.type.name, 'local'))
    return (globalVariablesList, localVariablesList)

def returnVariableDeclarations(sourceCodeDirectory):
    globalVariablesList = []
    localVariablesList = []
    tree = parse(sourceCodeDirectory)
    for path, node in tree.filter(javalang.tree.FieldDeclaration):
        globalVariablesList.append(node)
    
    tree = parse(sourceCodeDirectory)
    for path, node in tree.filter(javalang.tree.LocalVariableDeclaration):
        localVariablesList.append(node)
    return (globalVariablesList, localVariablesList)