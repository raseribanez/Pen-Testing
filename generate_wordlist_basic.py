#1/usr/bin/env/python
# Ben Woodfield

# A simpler list generator...creates as many possible instances of 'abc'
# Without re-using letters

import itertools

res = itertools.permutations('abc',5) # 5 is the length of your results characters (5 letters long)
for i in res: 
   print ''.join(i)
