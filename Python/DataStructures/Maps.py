#file that implements maps

#generates an instance object dict
def mapper():
    exec("class box:\n\tpass")
    exec("f = box()")
    return locals()["f"]

def addentry(obj, key, val):
    obj.__dict__[key] = val
def delentry(obj, key):
    del obj.__dict__[key]

def create_map(keys, vals):
    mapp = mapper()
    assert len(keys) == len(vals)
    for i in range(len(keys)):
        addentry(mapp, keys[i], vals[i])

#simple map node class, with an entry point and list of conenctions
class mapnode (object):

    def __init__(self, value):
        self.value = value
    def addnode(self, val):
        self.__dict__[val] = mapnode(val)
        self.__dict__[val].__dict__[self.value] = self
    def getnames(self):
        return list(self.__dict__.keys())
    @property
    def getnodes(self):
        return [self.__dict__[elem] for elem in self.__dict__.keys()]
