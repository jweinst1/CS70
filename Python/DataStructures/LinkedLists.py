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