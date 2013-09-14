#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 34 from projectEuler.net.
#   Finds the sum of all the numbers that can be expressed as the sum
#   of the factorial of its digits.
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

factorials = {
    0: 1,
    1:1,
    2:2,
    3:6,
    4:24,
    5:120,
    6:720,
    7:5040,
    8:40320,
    9:362880
    }

def find_limit():
    limit = '9'
    while factorials[9] * len(limit) > int(limit):
        limit += '9'
    return int(limit)

def is_sum_of_factorial_digits(n):
    sum_d = 0
    for digit in str(n):
        sum_d += factorials[int(digit)]
        if sum_d > n:
            return False
    if sum_d == n:
        return True
    return False

if __name__ == '__main__':
    limit = find_limit()
    result = sum(i for i in range(10, limit + 1) if is_sum_of_factorial_digits(i))
    print("The result is:", result)
