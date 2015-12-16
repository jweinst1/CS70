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

class glist:

    def __init__(self, *nodes):
        self.nodes = [elem for elem in nodes]
    def __repr__(self):
        return str(self.nodes)
    def __str__(self):
        return str(self.nodes)
    def __getitem__(self, item):
        return self.nodes[item]
    #adds a value as a node to the end of a graph line
    def append(self, i, value):
        current = self.ndoes[i]
        while current.direct != None:
            current = current.direct
        current.direct = gnode(value)
        return True
    
#conjoins two nodes together
def conjoin(n1, n2):
    n1.direct = n2
#straight line of ndoes
def conjoinlst(lst):
    lst = lst_nodes(lst)
    glst = lst.pop(0)
    current = glst
    while len(lst) > 0:
        current.direct = lst.pop(0)
        current = current.direct
    return glst

#takes a list, and converts each element to a node, which directs to one of the nodes in the gline
def attachlst(lst, gline):
    lst = lst_nodes(lst)
    current = gline
    while current.direct != None:
        node = gnode(lst.pop(0))
        node.direct = current
        current = current.direct
    return gline

#takes a graph line and attaches another gline to it at some index i
def attachline(gline1, gline2, i):
    current2 = gline2
    while current2.direct != None:
        current2 = current2.direct
    current1 = gline1
    while i > 0:
        current1 = current1.direct
    current2.direct = current1
    return gline1

#makes all the elements in the list into nodes and directs them all to node
def multi_attach(lst, node):
    lst = lst_nodes(lst)
    for elem in lst:
        elem.direct = node


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
