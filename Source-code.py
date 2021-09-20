import javalang

def tokenize(sourceCodeDirectory):
    sourceCode = open(sourceCodeDirectory, 'r').read()
    tokensList = list(javalang.tokenizer.tokenize(sourceCode))
    return tokensList

def parse(sourceCodeDirectory):
    sourceCode = open(sourceCodeDirectory, 'r').read()
    tree = javalang.parse.parse(sourceCode)
    return tree

tree = parse("Demo.java")
for path, node in tree.filter(javalang.tree.MethodDeclaration):
    print(path)
    print(node.position)
