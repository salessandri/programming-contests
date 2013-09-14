#!/usr/bin/env python3

########################################################################
#   Solves problem 21 from projectEuler.net.
#   Finds the sum of all the amicable numbers below 1000.
#   Copyright (C) 2010  Santiago Alessandri
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
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

def get_proper_divisors(n):
    result = [1]
    limit = int(n ** (0.5))
    for i in range(2, limit):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    if n % limit == 0:
        result.append(limit)
    return result

def is_amicable(n):
    pd = get_proper_divisors(n)
    sum_pd = 0
    for i in pd:
        sum_pd += i
    if sum_pd != n:
        sum_pd2 = 0
        for i in get_proper_divisors(sum_pd):
            sum_pd2 += i
        if sum_pd2 == n:
            return True
    return False

if __name__ == '__main__':
    result = 0
    for i in range(1, 10000):
        if is_amicable(i):
            result += i
    print("The result is:", result)
