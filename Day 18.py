#!/usr/bin/env python
# coding: utf-8

# In[95]:


import re
import numpy as np

def read_file(name):
    return [line.rstrip('\n') for line in open(name)]

def structure_line(line):
    group_of_groups = {0:[0]}
    groups = ['']*(line.count(r'(')+1)
    c_p = 0
    c_i = 0
    for i in [c for c in line if c != ' ']:
        if i == "(":
            c_p += 1
            c_i += 1
            if c_p not in group_of_groups:
                group_of_groups[c_p] = []
            group_of_groups[c_p].append(c_i)
            groups[max(group_of_groups[c_p-1])] += 'group_' + str(max(group_of_groups[(c_p)]))
        elif i == ")":
            c_p -= 1
        else:
            groups[max(group_of_groups[c_p])] += str(i)
    groups.reverse()
    return groups


# In[100]:


def day18a():
    data = read_file('input/18.txt')
    #data = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
    values = []
    for line in data:
        groups = structure_line(line)
        group_names = {}
        for i, group in enumerate(groups):
            for k,v in group_names.items():
                group = group.replace(k,str(v))
            group_num = len(groups)-i-1
            while '*' in group or '+' in group:
                part = re.search('([0-9]+[+*])([0-9]+)', group)
                group = str(eval(group[part.start():part.end()]))+group[part.end():]
            group_names['group_'+str(group_num)] = int(group)
        values.append(group_names['group_0'])
    return np.sum(values, dtype=np.int64)
get_ipython().run_line_magic('timeit', 'day18a()')
day18a()


# In[106]:


def day18b():
    data = read_file('input/18.txt')
    #data = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
    values = []
    for line in data:
        groups = structure_line(line)
        group_names = {}
        for i, group in enumerate(groups):
            for k,v in group_names.items():
                group = group.replace(k,str(v))
            group_num = len(groups)-i-1
            while '+' in group:
                part = re.search('([0-9]+[+])([0-9]+)', group)
                group = group[:part.start()]+str(eval(group[part.start():part.end()]))+group[part.end():]
            while '*' in group:
                part = re.search('([0-9]+[*])([0-9]+)', group)
                group = group[:part.start()]+str(eval(group[part.start():part.end()]))+group[part.end():]
            group_names['group_'+str(group_num)] = int(group)
        values.append(group_names['group_0'])
    return np.sum(values, dtype=np.int64)
get_ipython().run_line_magic('timeit', 'day18b()')
day18b()


# In[ ]:




