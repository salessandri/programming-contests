#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 66 from projectEuler.net.
#   Finds the D whose Pell's equation minimal solution has the highest X.
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

def continued_fraction(n):
    m = 0
    d = 1
    a = a_0 = int(n ** 0.5)
    triple_set = list()
    while (m, d, a) not in triple_set:
        triple_set.append((m, d, a))
        tmp_m = d * a - m
        tmp_d = (n - tmp_m ** 2) // d
        tmp_a = int((a_0 + tmp_m) / tmp_d)
        a = tmp_a
        d = tmp_d
        m = tmp_m
    triple_set.append((m, d, a))
    return triple_set

def min_x(n):
    resolution = continued_fraction(n)
    restart_index = resolution.index(resolution[-1])
    index = min(2, len(resolution) - 1)
    stored_x = []
    stored_y = []
    x = resolution[0][2]
    y = 1
    if x ** 2 - n * (y ** 2) == 1:
        return x
    stored_x.append(x)
    stored_y.append(y)
    x = resolution[0][2] * resolution[1][2] + 1
    y = resolution[1][2]
    while x ** 2 - n * (y ** 2) != 1:
        stored_x.append(x)
        stored_y.append(y)
        x = resolution[index][2] * x + 1 * stored_x[-2]
        y = resolution[index][2] * y + 1 * stored_y[-2]
        index += 1
        if index == len(resolution):
            index = restart_index + 1
    return x

if __name__ == '__main__':
    max_x = 0
    result = 0
    for d in filter(lambda d: int(d ** 0.5) ** 2 != d, range(1, 1001)):
        tmp = min_x(d)
        if tmp > max_x:
            max_x = tmp
            result = d
    print("The result is:", result)
    


