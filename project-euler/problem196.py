#!/usr/bin/env python3

########################################################################
#   Solves problem 196 from projectEuler.net.
#   Finds the sum of primes participating in a prime triplet.
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

from CommonFunctions import find_primes_less_than
from itertools import takewhile

primes = find_primes_less_than(6 * (10 ** 6))
primes_set = set(primes)

def primes_in_range(from_, to_):

    p_limit = (to_ + 1) ** (0.5)
    prime_set = set(range(from_, to_ + 1))
    for p in takewhile(lambda x: x <= p_limit, primes):
        mod = from_ % p
        start_n = from_ + (0 if mod == 0 else p - mod)
        for i in range(start_n, to_ + 1, p):
            prime_set.discard(i)
    
    return prime_set

sum_n = lambda n: n * (n + 1) // 2

def get_row_limits(n):
    from_ = sum_n(n-1) + 1
    to_ = sum_n(n)
    return (from_, to_)

def up_neighbours(n, row):
    from_, to_ = get_row_limits(row)
    offset = n - from_
    from_, to_ = get_row_limits(row - 1)
    results = set()
    if offset > 0:
        results.add(from_ + offset - 1)
    if from_ + offset <= to_:
        results.add(from_ + offset)
    if from_ + offset + 1 <= to_:
        results.add(from_ + offset + 1)
    
    return results

def down_neighbours(n, row):
    from_, to_ = get_row_limits(row)
    offset = n - from_
    from_, to_ = get_row_limits(row + 1)
    results = set()
    if offset > 0:
        results.add(from_ + offset - 1)
    results.add(from_ + offset)
    results.add(from_ + offset + 1)
    
    return results

def primes_in_triangles_of_row(row):
    f, t = get_row_limits(row)
    row_primes = primes_in_range(f, t)
      
    f, t = get_row_limits(row-1)
    up_row_primes = primes_in_range(f, t)
    
    f, t = get_row_limits(row-2)
    up_up_row_primes = primes_in_range(f, t)
    
    f, t = get_row_limits(row+1)
    down_row_primes = primes_in_range(f, t)
    
    f, t = get_row_limits(row+2)
    down_down_row_primes = primes_in_range(f, t)
    
    result = 0
    
    for p in row_primes:
        p_res = False
        up_primes = up_neighbours(p, row) & up_row_primes
        down_primes = down_neighbours(p, row) & down_row_primes
        if up_primes and down_primes:
            p_res = True
        
        if not p_res and (len(up_primes) > 1 or len(down_primes) > 1):
            p_res = True
        
        if not p_res:
            for up_p in up_primes:
                up_p_up_primes = up_neighbours(up_p, row-1) & up_up_row_primes
                if up_p_up_primes:
                    p_res = True
                    break
                up_p_down_primes = down_neighbours(up_p, row-1) & row_primes
                if len(up_p_down_primes) > 1:
                    p_res = True
                    break
        if not p_res:
            for down_p in down_primes:
                down_p_down_primes = down_neighbours(down_p, row+1) & down_down_row_primes
                if down_p_down_primes:
                    p_res = True
                    break
                down_p_up_primes = up_neighbours(down_p, row+1) & row_primes
                if len(down_p_up_primes) > 1:
                    p_res = True
                    break
        if p_res:
            result += p
            
    return result


if __name__ == '__main__':
    result = primes_in_triangles_of_row(5678027) + primes_in_triangles_of_row(7208785)
    print("The result is:", result)

