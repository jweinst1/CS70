#file the implements graphs and physical traversal graphs

#classes

class gnode:

    def __init__(self, value, direct=None):
        self.value = value
        self.direct = None
    def __repr__(self):
        return str(self.value) + "->" + str(self.direct)
    def __str__(self):
        return str(self.value) + "->" + str(self.direct)

#conjoins two nodes together
def conjoin(n1, n2):
    n1.direct = n2

def lst_nodes(lst):
    return [gnode(elem) for elem in lst]

#takes two lists, and connects each node in one lst to the node in the other lst
def zip_graph(lst1, lst2):
    assert len(lst1) == len(lst2)
    lst1 = [gnode(elem) for elem in lst1]
    lst2 = [gnode(elem) for elem in lst2]
    for i in range(len(lst1)):
        conjoin(lst1[i], lst2[i])
    return lst1
