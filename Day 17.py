#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
def read_file(name):
    return [line.rstrip('\n').replace('#', '1').replace('.', '0') for line in open(name)]


# In[69]:


def extend_data_3d(data, cycles):
    cube = np.zeros((len(data[0])+2*cycles,len(data)+2*cycles,1+2*cycles))
    check = cube[cycles:cycles+len(data[0]),cycles:cycles+len(data),cycles]
    for i, r in enumerate(data):
        for p, c in enumerate(r):
            check[i,p] = c
    return cube

def run_state_change_3d(cube):
    new_state = cube.copy()
    directions = []
    for x in range(-1,2,1):
        for y in range(-1,2,1):
            for z in range(-1,2,1):
                if not (x == 0 and y == 0 and z == 0):
                    directions.append([x,y,z])
    for ri, r in enumerate(cube):
        for ci, c in enumerate(r):
            for zi, z in enumerate(c):
                check_list = []
                for direction in directions:
                    sri = ri+direction[1]
                    sci = ci+direction[0]
                    szi = zi+direction[2]
                    if (0 <= sri < len(cube)) and (0 <= sci < len(r)) and (0 <= szi < len(c)):
                        check_list.append(cube[sri,sci,szi])
                if sum(check_list) not in [2,3] and z == 1:
                    new_state[ri,ci,zi] = 0
                if sum(check_list) == 3 and z == 0:
                    new_state[ri,ci,zi] = 1
    return new_state

def day17a(cube, cycles):
    for cycle in range(cycles):
        cube = run_state_change_3d(cube)
    return np.sum(cube, dtype=np.int64)
get_ipython().run_line_magic('timeit', "day17a(extend_data_3d(read_file('input/17.txt'), 6), 6)")
day17a(extend_data_3d(read_file('input/17.txt'), 6), 6)


# In[ ]:


def extend_data_4d(data, cycles):
    cube = np.zeros((len(data[0])+2*cycles,len(data)+2*cycles,1+2*cycles,1+2*cycles))
    check = cube[cycles:cycles+len(data[0]),cycles:cycles+len(data),cycles, cycles]
    for i, r in enumerate(data):
        for p, c in enumerate(r):
            check[i,p] = c
    return cube

def run_state_change_4d(cube):
    new_state = cube.copy()
    directions = []
    for x in range(-1,2,1):
        for y in range(-1,2,1):
            for z in range(-1,2,1):
                for f in range(-1,2,1):
                    if not (x == 0 and y == 0 and z == 0 and f == 0):
                        directions.append([x,y,z,f])
    for ri, r in enumerate(cube):
        for ci, c in enumerate(r):
            for zi, z in enumerate(c):
                for fi, f in enumerate(z):
                    check_list = []
                    for direction in directions:
                        sri = ri+direction[1]
                        sci = ci+direction[0]
                        szi = zi+direction[2]
                        sfi = fi+direction[3]
                        if (0 <= sri < len(cube)) and (0 <= sci < len(r)) and (0 <= szi < len(c)) and (0 <= sfi < len(z)):
                            check_list.append(cube[sri,sci,szi,sfi])
                    if sum(check_list) not in [2,3] and f == 1:
                        new_state[ri,ci,zi, fi] = 0
                    if sum(check_list) == 3 and f == 0:
                        new_state[ri,ci,zi,fi] = 1
    return new_state

def day17b(cube, cycles):
    for cycle in range(cycles):
        cube = run_state_change_4d(cube)
    return np.sum(cube, dtype=np.int64)
#%timeit day17b(extend_data_4d(read_file('input/17.txt'), 6), 6)
day17b(extend_data_4d(read_file('input/17.txt'), 6), 6)


# In[ ]:




