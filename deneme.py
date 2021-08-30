sourceFile = open('demo.txt', 'w')
print('Hello, Python!', file = sourceFile)
print('Hello, Python2!', file = sourceFile)
sourceFile.close()