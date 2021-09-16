import javalang

def tokenize(sourceCodeDirectory):
    sourceCode = open('Test-class.java', 'r').read()
    tokensList = list(javalang.tokenizer.tokenize(sourceCode))
    return tokensList

test = tokenize("Test-class.java")
for t in test:
    print(t)