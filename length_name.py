# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:53:49 2018

@author: Sveta
"""

# отсортировать по суммарной длине имени
x = [
     {"Guido", "van", "Rossum"},
     {"Hascell", "Curry"},
     {"John", "Bascus"}
     ]
###########################
#def length(name):
#    return len(" ".join(name))

#name_length =[length(name) for name in x]
#print(name_length)

## передали функцию length в качестве ключа сортировки
#x.sort(key = length)
#print(x)
###################################
## с помощью lambda- функции
x.sort(key = lambda name: len(" ".join(name)))
print(x)


