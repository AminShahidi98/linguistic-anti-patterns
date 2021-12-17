from Utils import *
from Models import *
from Detectors import *
from Actuators import *
import javalang
import inflect


'''
a = findMethodDeclarations('Demo.java')
b = createGetMethodComplement('Demo.java', a[1])
for i in b:
    print(i)
print("*************************************************")
'''


a = findMethodDeclarations('Demo.java')
for x in a:
    print(x.position)
    print('********************************************')


#insertGetMethodComplement('Demo.java')

'''
test=['public static int testTestTest(int x) {', 'return x;', '}']
a = insertMethodToTheEnd('Demo.java', test)
'''
'''
tree = parse('Demo.java')
for path, node in tree:
    print(node)
    print('************************************************************************************************')
'''
'''
f = open('Demo.java', 'r')
for i in f:
    if i == '\n':
        print('noneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    else:
        print(i)
'''

'''
x = findMethodDeclarations('Demo.java')
for i in x:
    print(i.modifiers)
    if 'static' in i.modifiers:
        print("yes")
    print('**********************************************************')
'''

'''
x = returnVariableDeclarations("Demo.java")
for pn in x[0]:
    for n in pn.declarators:
        print(n)
        print(pn.type.name)
        print(returnIfType13LAP(pn,n))
        print("******************")

for pn in x[1]:
    for n in pn.declarators:
        print(n)
        print(pn.type.name)
        print(returnIfType13LAP(pn,n))
        print("******************")
'''

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