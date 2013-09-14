#!/usr/bin/env python3

########################################################################
#   Solves problem 303 from projectEuler.net.
#   Finds the sum of the lower m for each n <= 10000 that makes
#   m * n have all digits < 3.
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

import heapq

LIMIT = 10000

mult_digit = {}
for i in range(10):
    mult_digit[i] = {}
    for j in range(10):
        if (i * j) % 10 not in mult_digit[i]:
            mult_digit[i][(i * j) % 10] = []
        mult_digit[i][(i * j) % 10].append(j)

def find_mult(i):
    str_i = str(i)
    heap = []
    for r in range(3):
        heap.extend((2, [j], i * j) for j in mult_digit[int(str_i[-1])].get(r, []))
    heapq.heapify(heap)
    used_set = set()
    while True:
        next_affected, list_n, parcial_mult = heapq.heappop(heap)
        
        if list_n[0] != 0 and max(str(parcial_mult)) < '3':
            return int(''.join(map(str, list_n)))
            
        if tuple(list_n[:len(str_i)+1]) in used_set:
            continue
        used_set.add(tuple(list_n[:len(str_i)+1]))
        
        str_parcial_mult = str(parcial_mult)
        try:
            s = int(str_parcial_mult[-next_affected])
        except IndexError:
            s = 0
        for d in range(3):
            d -= s
            d %= 10
            for mult in mult_digit[int(str_i[-1])].get(d, []):
                new_list_n = [mult] + list_n
                heapq.heappush(heap, (next_affected + 1, new_list_n, parcial_mult + mult * i * (10 ** (next_affected - 1))))

if __name__ == '__main__':
    result = sum(find_mult(i) for i in range(1, LIMIT + 1))
    print("The result is:", result)
