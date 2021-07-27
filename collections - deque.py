from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque

#Counter
str1 = 'aaabbbcccddddeeeeeee'
counter = Counter(str1)
print(counter)
print(counter.keys())
print(counter.values())
print(counter.most_common(2)[1][1])
print(list(counter.elements()))


#namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(4, 5)
pt = Point(5, 7)
print(pt)
print(pt.x, pt.y)

#defaultdict
"""returns zero if a key called 
which is not in the dictionary instead of 
throwing KeyError in normal dictionary """
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

#deque
"""Deque is preferred over list in the cases where 
we need quicker append and pop operations from 
both the ends of container, as deque provides a
n O(1) time complexity for append and pop operations
as compared to list which provides O(n) time complexity."""
d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)

#appendleft() adds item to the left of container
d.appendleft(11)
#print(d)

#pop() removes last element
#d.pop()
#print(d)

#clear() clears all elements in the list
#d.clear()
#print(d)

#extend() adds a list elements to the end of list
d.extend(['extend',4, 5, 6])
print(d)

#extendleft adds a list of elements to the beginning of container
d.extendleft([8, 7, 6, 'left'])
print(d)

#rotate moves all elements to 1 place to left
d.rotate()
print(d)

#-1 rotates all elemets to 1 place to right
d.rotate(-1)
print(d)
