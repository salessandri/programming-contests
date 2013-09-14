#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 64 from projectEuler.net.
#   Finds how many continued fractions for N <= 10000 have an odd period.
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

if __name__ == '__main__':
    result = 0
    for n in filter(lambda x: int(x ** 0.5) ** 2 != x, range(1, 10001)):
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
        while triple_set[0] != (m, d, a):
            triple_set.pop(0)
        if len(triple_set) & 1:
            result += 1
    print("The result is:", result)

