#binary tree implementation
class node(object):

    def __init__(self, head, left=None, right=None):
        self.head = head
        self.left = left
        self.right = right

def left_branch(lst):
    bt = node(lst.pop())
    current = bt
    while lst != []:
        current.left = node(lst.pop())
        current = current.left
    return bt

def append_right(bt, val, branch):
    current = bt
    while current != None:
        if current.head == branch:
            current.right = val
        else:
            current = current.left
    raise ValueError("branch not found")

