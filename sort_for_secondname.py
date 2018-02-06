# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:44:51 2018

@author: server1
"""

#остротировать по фамилии
x = [
     ("Guido", "van", "Rossum"),
     ("Hascell", "Curry"),
     ("John", "Bascus")
     ]
######################
#import operator as op
#x.sort(key = op.itemgetter(-1)) # это всегда обращение к последнему элементу списка
#print(x)
######################
import operator as op
from functools import partial

sort_by_last = partial(list.sort, key = op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)

y = ["abc", "cba", "abb"]
sort_by_last(y)
print(y)