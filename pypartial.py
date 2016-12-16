"""
PyPartial is a library that allows arbitrary
partial application of functions.
"""

class PartiallyAppliedFunction:
    def __init__(self, function, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.function = function
        self.__name__ = "<partial " + self.function.__name__ + "(" + self._argstr() + ")>"
    def __call__(self, *args, **kwargs):
        arguments = list(self.args)
        kwarguments = {}
        kwarguments.update(self.kwargs)
        kwarguments.update(kwargs)
        position = 0
        for i in range(len(arguments)):
            if arguments[i] == Ellipsis:
                arguments[i] = args[position]
                position += 1
        return self.function(*tuple(arguments),**kwarguments)
    def _argstr(self):
        argstr = ",".join(map(lambda x: "..." if x == Ellipsis else str(x), self.args))
        strls = []
        for key,value in self.kwargs.items():
            strls.append(str(key)+"="+str(value))
        kwargstr = ",".join(strls)
        finalstr = argstr
        if kwargstr:
            finalstr = argstr + "," + kwargstr
        return finalstr
    def __repr__(self):
        return self.__name__
    def deapply(self):
        return self.function

class ComposedFunction:
    def __init__(self, f, g):
        self.f = f
        self.g = g
        self.__name__ = "<composed " + self.f.__name__ + " with " + self.g.__name__ + ">"
    def __call__(self,*args,**kwargs):
        return self.f(self.g(*args,**kwargs))
    def __repr__(self):
        return self.__name__
    def decompose(self):
        return (f,g)

class CurriedFunction:
    def __init__(self, f, n, a):
        self.function = f
        self.empty = n
        self.args = a
        self.__name__ = "<curried " + self.function.__name__ + self._argstr() + ">"
    def __call__(self, arg):
        new_args = self.args + (arg,)
        if self.empty == 1:
            return self.function(*new_args)
        return CurriedFunction(self.function,self.empty-1,new_args)
    def _argstr(self):
        finalstr = ""
        for arg in self.args:
            finalstr = finalstr + "("+str(arg)+")"
        for slot in range(self.empty):
            finalstr = finalstr + "(...)"
        return finalstr
    def __repr__(self):
        return self.__name__
            

def curry(function,number):
    return CurriedFunction(function, number, ())

def apply(function,*args,**kwargs):
    return PartiallyAppliedFunction(function, *args, **kwargs)

def compose(*args):
    if len(args) < 2:
        raise TypeError("Not enough arguments")
    elif len(args) == 2:
        return ComposedFunction(args[0], args[1])
    else:
        return ComposedFunction(args[0], compose(*args[1:]))
