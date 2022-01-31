from Utils import *
from Models import *
from Detectors import *
from Actuators import *
#from Core import *
import javalang
import inflect

x = returnVariableDeclarators('Demo.java')
for i in x[0]:
    print(i)
    print('***')
print("////////////////////////////////////////////////////////////////////")
for i in x[1]:
    print(i)
    print('***')
print("////////////////////////////////////////////////////////////////////")
print("////////////////////////////////////////////////////////////////////")
print("////////////////////////////////////////////////////////////////////")
x = returnVariableDeclarations('Demo.java')
for i in x[0]:
    print(i)
    print('***')
print("////////////////////////////////////////////////////////////////////")
for i in x[1]:
    print(i)
    print('***')

'''
x = findMethodDeclarations('Demo.java')
for i in x:
    print(list(i.modifiers))
    print("**********************************************")'''

#"<class 'javalang.tree.ReturnStatement'>"
#"<class 'javalang.tree.IfStatement'>"
#"<class 'javalang.tree.BlockStatement'>"           
'''
        for x in i.body:
            print(x)
            print("--------------------------------------")
'''

#print(createGetMethodComplementName('public static int getisDobed(int d) {'))

'''
a = findMethodDeclarations('Demo.java')
b = createGetMethodComplement('Demo.java', a[2])
insertMethodToTheEnd('Demo.java', b)
'''

'''
a = findMethodDeclarations('Demo.java')
b = createGetMethodComplement('Demo.java', a[2])
for i in b:
    print(i)
print("*************************************************")
'''
'''
a = findMethodDeclarations('Demo.java')
for x in a:
    print(x.position)
    print('********************************************')
'''

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