from Utils import *
from Models import *
from Detectors import *
import javalang
import inflect

class Void():
    def __init__(self, name):
        self.name = 'void'
void = Void('void')

test = findMethodDeclarations("Demo.java")
for t in test:
    print(t.name)
    print(t.body)
    print("****************************")