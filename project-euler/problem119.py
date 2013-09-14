#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 119 from projectEuler.net.
#   Find the 30th number that is a power of the sum of its digits
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
    cant = 0
    number_array = [x ** 2 for x in range(2, 150)]
    while cant < 30:
        min_n = min(number_array)
        ind_min = number_array.index(min_n) + 2
        if sum(int(x) for x in str(min_n)) == ind_min:
            cant += 1
        number_array[ind_min - 2] *= ind_min
    print("The result is:", min_n)

