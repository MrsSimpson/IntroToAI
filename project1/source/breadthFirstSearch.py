from source.newNode import Node

def createRoot(theQ):
    if theQ  == None:
        root = Node()
        theQ = root

    return theQ

def createQueue(Node):
    theQ = list()
    if theQ == None:
        root = createRoot(theQ)
    else:
        theQ.append(Node)

def isQueueEmpty(theQ):
    if theQ == None:
        return True
    else:
        return False

