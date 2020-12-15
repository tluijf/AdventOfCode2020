#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict
day15input = [13,0,10,12,1,5,8]
def day15(data, nth=2020):
    turns = defaultdict(list)
    counts = defaultdict(int)
    last_num = 0
    for i in range(nth):
        t = data[i] if i < len(data) else 0 if counts[last_num] == 1 else turns[last_num][0]-turns[last_num][1]
        turns[t] = [i, turns[t][0] if t in turns else 0]
        counts[t] += 1
        last_num = t
    return last_num
get_ipython().run_line_magic('timeit', 'day15(day15input, 2020)')
print('part 1', day15(day15input, 2020))
get_ipython().run_line_magic('timeit', 'day15(day15input, 30000000)')
print('part 2', day15(day15input, 30000000))
