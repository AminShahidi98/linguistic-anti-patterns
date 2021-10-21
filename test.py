from Utils import *
from Models import *
from Detectors import *
import javalang
import inflect

class Void():
    def __init__(self, name):
        self.name = 'void'
void = Void('void')

tree = parse("Demo.java")
for path, node in tree:
    print(t.name)
    print(t.body)
    print("****************************")