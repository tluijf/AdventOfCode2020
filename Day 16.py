#!/usr/bin/env python
# coding: utf-8

# In[98]:


import re
import numpy as np
def read_file(name):
    return [line.rstrip('\n') for line in open(name)]


# In[99]:


def day16a(data):
    allowed_ranges = set()
    error_rate = 0
    for r in [d for d in data if d != ""]:
        if not r[0].isdigit():
            field = r.split(':')
            ranges = re.findall('(\d+)', field[1])
            allowed_ranges.update([d for i in range(0, len(ranges),2) for d in range(int(ranges[i]), int(ranges[i+1])+1)])
        else:
            error_rate += sum([int(i) for i in r.split(',') if int(i) not in allowed_ranges])
    return error_rate
get_ipython().run_line_magic('timeit', "day16a(read_file('input/16.txt'))")
day16a(read_file('input/16.txt'))


# In[128]:


def day16b(data):
    ticket_fields = {}
    available_fields = {}
    allowed_ranges = set()
    for ri, r in enumerate([d for d in data if d != ""]):
        if not r[0].isdigit():
            if 'your ticket:' in r:
                own_ticket = [int(i) for i in data[ri+2].split(',')]
            elif 'nearby tickets' not in r:
                field = r.split(':')
                ranges = re.findall('(\d+)', field[1])
                f = [d for i in range(0, len(ranges),2) for d in range(int(ranges[i]), int(ranges[i+1])+1)]
                allowed_ranges.update(f)
                ticket_fields[field[0]] = f
                available_fields[field[0]] = None
        else:
            fields = [int(i) for i in r.split(',')]
            errors = [i for i in fields if i not in allowed_ranges]
            if errors == []:
                for i, field in enumerate(fields):
                    for k, v in ticket_fields.items():
                        if available_fields[k] == None:
                            available_fields[k] = [i for i in range(len(own_ticket))]
                        if field not in v and i in available_fields[k]:
                            available_fields[k].remove(i)
    too_many = 1
    while too_many > 0:
        too_many = len(available_fields.keys())
        for k,v in available_fields.items():
            if len(v) == 1:
                available_fields = {kk:[i for i in vv if i not in v or kk == k] for kk,vv in available_fields.items()}
                too_many -= 1
    needed_fields = [own_ticket[v[0]] for k,v in available_fields.items() if 'departure' in k]
    return np.prod(needed_fields, dtype=np.int64)
get_ipython().run_line_magic('timeit', "day16b(read_file('input/16.txt'))")
day16b(read_file('input/16.txt'))


# In[ ]:




