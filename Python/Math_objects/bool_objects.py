#file that contaisn bool objects

class statement(object):

    def __init__(self, statement):
        self.statement = statement
        self.bool = eval(statement)
    def __bool__(self):
        return self.bool
    def __repr__(self):
        return str(self.statement)

class expression(object):
    #creates an object, such that can be called on an input to see if it evaluates to true.

    def __init__(self, var, exp):
        self.var = var
        self.exp = exp
    def __call__(self, input):
        temp = self.var + " = " + str(input)
        exec(temp)
        return eval(self.exp)




