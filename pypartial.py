"""
PyPartial is a library that allows arbitrary 
partial application of functions.
"""

class PartiallyAppliedFunction:
    def __init__(self, function, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.function = function
        self.__name__ = "<partial_" + self.function.__name__ + ">"
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
    def __repr__(self):
        argstr = ', '.join([repr(i) if i is not ... else '...' 
                            for i in self.args])
        representation = [str(i) for i in 
                         [self.function.__name__,'(',argstr,')']]
        return ''.join(representation)
    def deapply(self):
        return self.function

class ComposedFunction:
    def __init__(self, f, g):
        self.f = f
        self.g = g
        self.__name__ = self.f.__name__ + " Applied To " + self.g.__name__
    def __call__(self,*args,**kwargs):
        return self.f(self.g(*args,**kwargs))
    def __repr__(self):
        representation = [str(i) for i in 
                         [self.f.__name__,'(',self.g.__name__,'(...)',')']]
        return ''.join(representation)
    def decompose(self):
        return (f,g)

def apply(function,*args,**kwargs):
    return PartiallyAppliedFunction(function, *args, **kwargs)

def compose(*args):
    if len(args) < 2:
        raise TypeError("Not enough arguments")
    elif len(args) == 2:
        return ComposedFunction(args[0], args[1])
    else:
        return ComposedFunction(args[0], compose(*args[1:]))

