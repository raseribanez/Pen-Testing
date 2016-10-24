#!/usr/bin/env/python
# Ben Woodfield

# Creates ALL possible instances (combinations) of 'abc', including
# the same letters more than once
 
import itertools

res = itertools.product('abc', repeat=5)# 5 characters long results
    print ''.join(i)

