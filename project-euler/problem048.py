#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 48 from projectEuler.net.
#   Finds the last 10 digits from the sum of 1^1 + 2^2 + ... + 1000^1000
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

from functools import reduce

if __name__ == '__main__':
    limiter = 10 ** 10
    red_func = lambda x, y: (x % limiter + y % limiter) % limiter
    result = reduce(red_func, (i ** i for i in range(1, 1001)))
    print("The result is:", result)
