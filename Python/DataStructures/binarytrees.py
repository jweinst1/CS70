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

#makes a btree by continously dividing n, recursively
def make_divnumtree(n):
    if n == 0:
        return None
    else:
        return branch(n, make_divnumtree(n//2), make_divnumtree(n//2))