#linked lists implementations

class fnode:
    #node that is always directed forward
    def __init__(self, head, forward=None):
        self.head = head
        self.forward = forward
    def __str__(self):
        return str(self.head) + "->" + str(self.forward)
    def __repr__(self):
        return str(self.head) + "->" + str(self.forward)
    def __len__(self):
        length = 1
        current = self
        while current.forward != None:
            length += 1
            current = current.forward
        return length
    def __getitem__(self, item):
        current = self
        while item > 0:
            if current.head == None:
                raise IndexError
            current = current.forward
            item -= 1
        return current.head

 #turns a list into a forward linked list
def const_flist(lst):
    flist = fnode(lst.pop(0))
    current = flist
    while len(lst) > 0:
        current.forward = fnode(lst.pop(0))
        current = current.forward
    return flist

def circular_flist(lst):
    #produces a circular list of forward nodes
    flist = fnode(lst.pop(0))
    current = flist
    while len(lst) > 0:
        current.forward = fnode(lst.pop(0))
        current = current.forward
    current.forward = flist
    return flist

#constructs forward linked list recusrively
def recursive_flist(lst):
    if len(lst) == 0:
        return None
    else:
        return fnode(lst.pop(0), recursive_flist(lst))

#FORWARD BACKWARD LISTS

class fbnode:
#node that has a forward and backward method, and two entry points
    def __init__(self, head, forward=None, backward=None):
        self.head = head
        self.forward = forward
        self.backward = backward
    def __str__(self):
        return str(self.head) + "<->" + str(self.forward)
    def __repr__(self):
        return str(self.head) + "<->" + str(self.forward)
    def list(self):
        values = []
        curent = self
        while current.forward != None:
            values.append(curent.head)
            current = current.forward
        return values

def const_fblist(lst):
    #constructs a forward-back list iteratively
    fbl = fbnode(lst.pop(0))
    current = fbl
    tracer = fbl
    while len(lst) > 0:
        current.forward = fbnode(lst.pop(0))
        current = current.forward
        current.backward = tracer
        tracer = current
    return fbl

def circ_fblist(lst):
    #constructs a forward-back list in a circular, infinite chain
    fbl = fbnode(lst.pop(0))
    current = fbl
    tracer = fbl
    while len(lst) > 0:
        current.forward = fbnode(lst.pop(0))
        current = current.forward
        current.backward = tracer
        tracer = current
    fbl.backward = current
    return fbl
#gets an item from a circular fblist, allows i to be any value, if it's higher
#than the length of the list, it starts over again
def getitem_fblc(forbacklst, i):
    current = forbacklst
    if i == 0:
        return forbacklst.head
    elif i > 0:
        while i > 0:
            current = current.forward
            i -=1
        return current.head
    elif i < 0:
        while i < 0:
            current = current.backward
            i += 1
        return current.head
    else:
        raise IndexError
