from pypartial import *
import math

onebasedrange = apply(range,1,...)
assert(list(onebasedrange(10)) == [1,2,3,4,5,6,7,8,9])

inclusiverange = compose(onebasedrange,lambda x: x + 1)
assert(list(inclusiverange(10)) == [1,2,3,4,5,6,7,8,9,10])

pow2 = apply(pow,2,...)
for i in range(10):
    assert(pow2(i) == pow(2,i))

absolute = compose(math.sqrt,lambda x: x*x,float)
assert(absolute(-1) == 1)
assert(absolute(-1.23) == 1.23)
assert(absolute("11") == 11)
assert(absolute("-3.1415") == 3.1415)

curried_range = curry(range,2)
otheronebased = curried_range(1)

assert(list(curried_range(1)(10)) == [1,2,3,4,5,6,7,8,9])
assert(otheronebased(11) == onebasedrange(11))
assert(otheronebased(2) == onebasedrange(2))
assert(otheronebased(100) == onebasedrange(100))
assert(otheronebased(34) != onebasedrange(35))

print(onebasedrange)
print(otheronebased)
print(curried_range)
print(inclusiverange)
