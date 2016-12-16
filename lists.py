import random
from pypartial import *

list_example = [[random.randrange(i+j+1) for i in range(100)] for j in range(100)]

#traditional way

def flip_and_cube(ls):
    newls = [[0 for i in ls] for i in ls[0]]
    for i in range(len(ls)):
        for j in range(len(ls)):
            newls[j][i] = ls[i][j]**3
    return newls

list1 = flip_and_cube(list_example)

#pypartial way

cubify = apply(map,lambda x: map(lambda y: y**3, x),...)
listify = compose(list,apply(map,lambda x: list(x),...))
flip = lambda z: [[z[j][i] for j in range(len(z))] for i in range(len(z[0]))]
final = compose(flip,listify,cubify)

list2 = final(list_example)

#compare

assert(list1 == list2)

print(final)
