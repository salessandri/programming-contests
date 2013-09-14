#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 44 from projectEuler.net.
#   Finds the tuple of triangular numbers whose addition and difference
#   is a triangular number.
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

from itertools import combinations

if __name__ == '__main__':
    pentag_list = [n * (3 * n - 1) // 2 for n in range(1, 5000)]
    setp = set(pentag_list)
    pares = [tupla for tupla in combinations(pentag_list, 2) if abs(tupla[0] - tupla[1]) in setp]
    for tupla in pares:
        suma = tupla[1] + tupla[0]
        while pentag_list[-1] < suma:
            n = len(pentag_list) + 1
            pentag_list.append(n * (3 * n -1) / 2)
        if suma in pentag_list:
            print("The result is:", abs(tupla[0] - tupla[1]))
