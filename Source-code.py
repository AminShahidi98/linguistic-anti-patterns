import javalang

def tokenize(sourceCodeDirectory):
    with open(sourceCodeDirectory) as sourceCode:
        tokensList = []
        for line in sourceCode:
            tokens = list(javalang.tokenizer.tokenize(line))
            for token in tokens:
                tokensList.append(token)
    return tokensList

test = tokenize("Test-class.java")
