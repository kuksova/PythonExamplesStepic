# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:49:52 2018

@author: server1
"""

f = open("test.txt","w")
lines = ["ab","c","d"]
contents = "\n".join(lines)
f.write(contents)
f.close()

k = open("test.txt")
xp = k.read()
x1 = k.readline()
x1 = x1.rstrip()
#print(k.readlines()[::-1])
with open("dataset_24465_4.txt") as b, open ("test1.txt", "w") as w:
   # y = b.readlines()[::-1]
    y = b.read().splitlines()[::-1]
    #y = y.rstrip()
    print(y)
   # for line in b:
    cont = "\n".join(y)
    w.write(cont)
#    print(repr(b.readlines()))
        #w.write()
k.close()
        