#binary trees file

class branch:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.left) + "<-"+ str(self.value) + "->" + str(self.right)
    def __repr__(self):
        return str(self.left) + "<-"+ str(self.value) + "->" + str(self.right)


class b_constructors:
#makes a btree by continously dividing n, recursively
    @staticmethod
    def make_divnumtree(n):
        if n == 0:
            return None
        else:
            return branch(n, b_constructors.make_divnumtree(n//2), b_constructors.make_divnumtree(n//2))
    #makes a btree by continuously subtracting 1 from n, recursively.
    @staticmethod
    def make_subtree(n):
        if n == 0:
            return None
        else:
            return branch(n, b_constructors.make_subtree(n-1), b_constructors.make_subtree(n-1))
    #makes btree by subtracting inter from n recursively
    @staticmethod
    def inter_subtree(n, inter):
        if n <= 0:
            return None
        else:
            return branch(n, b_constructors.inter_subtree(n-inter, inter), b_constructors(n-inter, inter))
    #makes a btree by starting at 1 and continuously adding 1 until n is reached
    @staticmethod
    def addtree(n, start=1):
        if start == n:
            return None
        else:
            return branch(start, b_constructors.addtree(n, start+1), b_constructors.addtree(n, start+1))

    @staticmethod
    def multree(n, multip, start=1):
        if start >= n:
            return None
        else:
            return branch(start, b_constructors.multree(n, multip, start*multip), b_constructors.multree(n, multip, start*multip))

    #makes a list into an even btree
    @staticmethod
    def listtree(lst):
        if len(lst) == 0:
            return None
        elif len(lst) == 1:
            return branch(lst[0])
        else:
            return branch(lst.pop(0), b_constructors.listtree(lst[:len(lst)//2]), b_constructors.listtree(lst[len(lst)//2:]))


#searches a btree with tree recursion
def search_btree(value, btree, btree2=None):
    if btree == None:
        return False
    elif btree.value == value:
        return True
    else:
        return search_btree(btree.left, value), search_btree(btree.right, value)
#prints all the nodes in a btree, starting at the root
def printallbtree(btree):
    if btree == None:
        return None
    else:
        print(btree.value)
        printallbtree(btree.left)
        printallbtree(btree.right)

#returns values for right most btree branch
def getright_branch(btree):
    values = []
    current = btree
    while current.right != None:
        values.append(current.value)
        current = current.right
    return values
#gets all values of left most branch in btree
def getleft_branch(btree):
    values = []
    current = btree
    while current.left != None:
        values.append(current.value)
        current = current.left
    return values

def getallvals(btree, lst=[]):
    if btree == None:
        return lst



#gets length of left most branch
def left_length(btree):
    return len(getleft_branch(btree))
#gets length of right most branch
def right_length(btree):
    return len(getright_branch(btree))
