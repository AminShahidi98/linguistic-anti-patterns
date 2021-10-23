from Utils import *
from Models import *
from Detectors import *
import javalang
import inflect


x = returnVariableDeclarations("Demo.java")
for pn in x[0]:
    for n in pn.declarators:
        print(n)
        print(returnIfType12or14LAP(pn,n))
        print("******************")

for pn in x[1]:
    for n in pn.declarators:
        print(n)
        print(returnIfType12or14LAP(pn,n))
        print("******************")

'''
x = returnVariableDeclarations("Demo.java")
for i in x[0]:
    print(i)

for j in x[1]:
    print(j)

tree = parse("Demo.java")
for path, node in tree.filter(javalang.tree.FieldDeclaration):
    for p, n in node.filter(javalang.tree.VariableDeclarator):
        print(node.position.line)
        print(n.name)
        print("****************************")

for path, node in tree.filter(javalang.tree.LocalVariableDeclaration):
    for p, n in node.filter(javalang.tree.VariableDeclarator):
        print(n.position.line)
        print(n.name)
        print("****************************")
'''