# HW2 - P3-3 ALPHA BETA PRUNING   (Osman Bulut-001530539)

class BinaryTree():

    def __init__(self, rootid, value):
        self.left = None
        self.right = None
        self.rootid = rootid
        self.value = value

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.value = value

    def getNodeValue(self):
        return self.value

    def getNodePlace(self):
        return self.rootid

    def insertRight(self, childid, newNode):
        self.right = BinaryTree(childid, newNode)

    def insertLeft(self, childid, newNode):
        self.left = BinaryTree(childid, newNode)


def testTree():
    myTree = BinaryTree("l_00", inf)
    myTree.insertLeft("l_10", ninf)
    myTree.insertRight("l_11", ninf)
    # layer 1
    l10 = myTree.getLeftChild()
    l10.insertLeft("l_20", inf)
    l10.insertRight("l_21", inf)

    l11 = myTree.getRightChild()
    l11.insertLeft("l_22", inf)
    l11.insertRight("l_23", inf)

    # layer2
    l20 = l10.getLeftChild()
    l20.insertLeft("l_30", ninf)
    l20.insertRight("l_31", ninf)

    l21 = l10.getRightChild()
    l21.insertLeft("l_32", ninf)
    l21.insertRight("l_33", ninf)

    l22 = l11.getLeftChild()
    l22.insertLeft("l_34", ninf)
    l22.insertRight("l_35", ninf)

    l23 = l11.getRightChild()
    l23.insertLeft("l_36", ninf)
    l23.insertRight("l_37", ninf)

    # layer 3
    l30 = l20.getLeftChild()
    l30.insertLeft("l_40", 3)
    l30.insertRight("l_41", 10)

    l31 = l20.getRightChild()
    l31.insertLeft("l_42", 2)
    l31.insertRight("l_43", 9)

    l32 = l21.getLeftChild()
    l32.insertLeft("l_44", 10)
    l32.insertRight("l_45", 7)

    l33 = l21.getRightChild()
    l33.insertLeft("l_46", 5)
    l33.insertRight("l_47", 9)

    l34 = l22.getLeftChild()
    l34.insertLeft("l_48", 2)
    l34.insertRight("l_49", 5)

    l35 = l22.getRightChild()
    l35.insertLeft("l_410", 6)
    l35.insertRight("l_411", 4)

    l36 = l23.getLeftChild()
    l36.insertLeft("l_412", 2)
    l36.insertRight("l_413", 7)

    l37 = l23.getRightChild()
    l37.insertLeft("l_414", 9)
    l37.insertRight("l_415", 1)

    return myTree


inf = 99999999
ninf = -99999999


def maximizer(current,alpha,beta):
    if current.getNodeValue() != inf and current.getNodeValue() != ninf:
        return current.getNodeValue()

    children = [current.getLeftChild(), current.getRightChild()]
    comp = ninf
    for i in children:
        eval = minimizer(i,alpha,beta)
        comp = max(comp, eval)
        alpha=max(alpha,eval)
        if beta <= alpha:
            break

    return comp


def minimizer(current,alpha,beta):
    if current.getNodeValue() != inf and current.getNodeValue() != ninf:
        return current.getNodeValue()

    children = [current.getLeftChild(), current.getRightChild()]

    comp = inf
    for i in children:
        eval = maximizer(i,alpha,beta)
        comp = min(comp, eval)
        beta=min(beta,eval)
        if beta<=alpha:
            break

    return comp


def path(root, id, winner):
    if (not root):
        return False

    id.append(root.rootid)

    if root.getNodeValue() == winner:
        return True

    if (path(root.getLeftChild(), id, winner) or path(root.getRightChild(), id, winner)):
        return True

    id.pop(-1)

    return False


def minimax(root, winner):
    id = []

    if path(root, id, winner)==True:
        print("The winner node is:",winner)
        print("The path is:")
        for i in range(len(id) - 1):
            print( id[i])
        print(id[len(id) - 1])

    else:
        print("No Path")

#We call maximizer because our root node is maximizer for this example

minimax(testTree(), maximizer(testTree(),ninf,inf))
