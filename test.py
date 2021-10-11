from Utils import *
from Models import *
from Detectors import *
import javalang

import inflect
inflect = inflect.engine()

print(isPlural("array"))


'''
test = findMethodDeclarations("Demo.java")
for t in test:
    if returnSetMethodSmell(t)=='setMethod' or returnGetMethodSmell(t)=='maybeSetMethod':
        print(returnSetLAPType(t))
        print(t.name)
        #print(t.return_type.name)
        print("****************************")'''