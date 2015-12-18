#implementation for a Hash table

class col_node:
   #linked node to deal with collisions
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return str(self.value)
    def __str__(self):
        return str(self.value)


class hashtable:
    #for storing values only
    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(size+1)]
    def __str__(self):
        return str(self.table)
    def __repr__(self):
        return str(self.table)
    @property
    def values(self):
        return [elem for elem in self.table if elem]
    @property
    def empty_slots(self):
        return [i for i in range(len(self.tables)) if not self.tables[i]]
    def put(self, value):
        #accounts for collisions with chaining
        hash_val = hashstring(value)
        if hash_val > self.size+1:
            hash_val %= self.size
            if not self.table[hash_val]:
                self.table[hash_val] = value
            else:
                self.table[hash_val] = col_node(self.table[hash_val])
                self.table[hash_val].next = value
        else:
            self.table[hash_val] = value
    def check(self, value):
        hash_val = hashstring(value)
        if hash_val > self.size+1:
            hash_val %= self.size
            if self.table[hash_val]:
                return True
            else:
                return False
        else:
            if self.table[hash_val]:
                return True
            else:
                return False
    def get(self, index):
        return self.table[index]

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

def hashstring(string):
    val = name_to_int(string)
    return collapse_int(val)

#table with keys and values
class hashkv_table:

    def __init__(self, size):
        self.size = size
        self.slots = [None for i in range(size+1)]
        self.data = [None for i in range(size+1)]