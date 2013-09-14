#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 56 from projectEuler.net.
#   Finds the maximum digital sum amon a ** b for a,b < 100
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

def digital_sum(n):
    return sum(int(c) for c in str(n))

if __name__ == '__main__':
    result = max(digital_sum(a ** b) for a in range(100) for b in range(100))
    print("The result is:", result)
