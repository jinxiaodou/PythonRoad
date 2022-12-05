import sys, os

def writeToFile(name,str):
    with open(sys.path[0]+'/'+name+'.txt', 'a', encoding='utf-8') as f:
        f.writelines(str)
        f.write('\n\n\n\n')

if __name__=='__main__':
    writeToFile('filename', 'Hello world!')