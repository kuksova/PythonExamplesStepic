# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:52:09 2018

@author: server1
"""

import os
import os.path
import shutil

lst = []
for current_dir, dirs, files in os.walk("main"):
    for str1 in files:
        if str1.endswith('.py'):
            if any(current_dir in s for s in lst):
                continue
            else:
                print(current_dir, dirs, files)
                lst.append(current_dir)
           # current_dir = current_dir.splitlines()
           

f = open("spisok.txt", "w")
lst.sort()
print(lst)
cont = "\n".join(lst)
f.write(cont)
f.close()
