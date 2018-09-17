from source.newNode import *

def createRoot(theQ):
    if theQ  == None:
        root = Node()
        theRoot = root

    return theRoot

def createQueue(Node):
    theQ = []
    if isQueueEmpty == True:
        root = createRoot(theQ)
        theQ.append(root)
    else:
        theQ.append(Node)

    return theQ

def isQueueEmpty(theQ):
    if theQ == None:
        return True
    else:
        return False




