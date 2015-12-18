#implementation for the ordered set in python

class osnode:

    def __init__(self, amount=0, element=None):
        self. element = element
        self.amount = amount
    def __repr__(self):
        return str(self.element) + "-" + str(self.amount)
    def __str__(self):
        return str(self.element) + "-" + str(self.amount)
    def amount(self):
        return self.amount

class orderedset:

    def __init__(self, size):
        self.size = size
        self.oset = [None for i in range(size+1)]

    def addelement(self, value, amount):
        hash_key = hashstring(value, self.size-1)
        elem = osnode(amount, value)
        self.oset[hash_key] = elem

    def increase(self, value, increment):
        hash_key = hashstring(value, self.size-1)
        self.oset[hash_key].amount += increment

    def getcount(self, value):
        hash_key = hashstring(value, self.size-1)
        return self.oset[hash_key].amount

    def __contains__(self, item):
        hash_key = hashstring(item, self.size-1)
        if not self.oset[hash_key]:
            return False
        else:
            return True

#Hashing functions
def collapse_int(num):
    numlst = list(str(num))
    numbers = [int(elem) for elem in numlst]
    return sum(numbers)

#converts a letter sequence into an integer
def name_to_int(string):
    import re
    string = string.lower()
    patterns = [r'a', r'b', r'c', r'd',
    r'e', r'f', r'g', r'h', r'i', r'j', r'k', r'l', r'm',
    r'n', r'o', r'p', r'q', r'r', r's',
    r't', r'u', r'v', r'w', r'x', r'y', r'z', r' ']
    numbers = [str(elem) for elem in range(1, 28)]
    for i in range(len(patterns)):
        string = re.sub(patterns[i], numbers[i], string)
    return int(string)
#hashes a string, and takes remainder to fit into the table.
def hashstring(string, hsize):
    val = name_to_int(string)
    return collapse_int(val) % hsize