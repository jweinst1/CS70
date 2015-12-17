#File for implementing Heaps

class hnode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.left) + "<-"+ str(self.value) + "->" + str(self.right)
    def __repr__(self):
        return str(self.left) + "<-"+ str(self.value) + "->" + str(self.right)
    def getrightval(self):
        if self.right != None:
            return self.right.value
        else:
            return False
    def getleftval(self):
        if self.left != None:
            return self.left.value
        else:
            return False

#tools
#checks if child nodes lower than value of parent node
def isheap(heap):
    if heap.left.value <= heap.value and heap.right.value <= heap.value:
        return True
    else:
        return False

def isleaf(heap):
    if heap.left == None and heap.right == None:
        return True
    else:
        return False
#swaps value of two heap nodes
def swapheaps(heap1, heap2):
    hold = heap1.value
    heap1.value = heap2.value
    heap2.value = hold

#removes and returns the max of a list
def get_max(lst):
    hold = max(lst)
    lst.remove(hold)
    return hold

class heap_cons:

    @staticmethod
    def lsttoheap(lst):
        if len(lst) == 0:
            return None
        elif len(lst) == 1:
            return hnode(lst[0])
        else:
            return hnode(lst.pop(0), heap_cons.lsttoheap(lst[:len(lst)//2]), heap_cons.lsttoheap(lst[len(lst)//2:]))
#converts a heap into order
def heapify(heap):
    if isleaf(heap):
        return heap
    elif heap.getrightval() > heap.value:
        swapheaps(heap, heap.right)
    elif heap.getleftval() > heap.value:
        swapheaps(heap, heap.left)
    else:
        heapify(heap.left)
        heapify(heap.right)

def appendheap(heap, item):
    pass