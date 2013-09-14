#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 45 from projectEuler.net.
#   Finds the second number which is triangular, pentagonal and hexagonal
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
    iT = 286
    iP = 166
    iH = 144
    
    t = iT * (iT + 1) // 2
    p = iP * (3 * iP - 1) // 2
    h = iH * (2 * iH - 1)
    
    while h != t or t != p:
        h = iH * (2 * iH - 1)
        iH += 1
        while t < h:
            t = iT * (iT + 1) // 2
            iT += 1
        while p < h:
            p = iP * (3 * iP - 1) // 2
            iP += 1
    print("The result is:", h)
    