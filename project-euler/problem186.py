#!/usr/bin/env python3

########################################################################
#   Solves problem 186 from projectEuler.net.
#   Finds how many phone calls are needed in order to have 99% of the 
#   graph connected including a particular vertex.
#   Copyright (C) 2011  Santiago Alessandri
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#	
#   You can contact me at san.lt.ss@gmail.com
#   Visit my wiki at http://wiki.san-ss.com.ar
#   Visit my blog at http://blog.san-ss.com.ar
########################################################################

from collections import deque

def generator():
    queue_55 = deque()
    queue_24 = deque()
    for k in range(1, 56):
        s_k = (100003 - 200003 * k + 300007 * (k ** 3)) % 1000000
        queue_55.append(s_k)
        if k >= 32:
            queue_24.append(s_k) 
        yield s_k
    while True:
        s_k = (queue_55.popleft() + queue_24.popleft()) % 1000000
        queue_55.append(s_k)
        queue_24.append(s_k) 
        yield s_k

graph_list = [set([i]) for i in range(1000000)]

def get_pos_of(i):
    while isinstance(graph_list[i], int):
        i = graph_list[i]
    return i

if __name__ == '__main__':
    gen = generator()
    res = 0
    while len(graph_list[get_pos_of(524287)]) < 990000:
        c1 = next(gen)
        c2 = next(gen)
        if c1 == c2:
            continue
        res += 1
        i1 = get_pos_of(c1)
        i2 = get_pos_of(c2)
        if i1 != i2:
            to_put_into = min(i1, i2)
            to_remove = max(i1, i2)
            graph_list[to_put_into] |= (graph_list[to_remove])
            graph_list[to_remove] = to_put_into        
    print("The result is:", res)
