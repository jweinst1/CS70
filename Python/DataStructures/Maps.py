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
class mapnode:

    def __init__(self, value, connections=[]):
        self.value = value
        self.connections = connections
    def addconnect(self, item):
        self.connections.append(mapnode(item))
    def getconencts(self):
        return [elem.value for elem in self.connections]