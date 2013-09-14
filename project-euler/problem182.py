#!/usr/bin/python3

########################################################################
#   Solves problem 182 from projectEuler.net.
#   Finds the sum of the exponents that give the less number of 
#   unconcealed messages for an n.
#   Copyright (C) 2012  Santiago Alessandri
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
#   You can contact me at san-ss@san-ss.com.ar
#   Visit my wiki at http://blog.san-ss.com.ar
########################################################################

import gmpy

if __name__ == '__main__':
    p = 1009
    q = 3643
    n = p * q
    phi_n = n - p - q + 1
    result = 0
    min_res = 9999999999999
    for e in range(1, phi_n):
        if gmpy.gcd(e, phi_n) != 1:
            continue
        num_unconcealed = (gmpy.gcd(e-1, p-1) + 1) * (gmpy.gcd(e-1, q-1) + 1)
        if num_unconcealed < min_res:
            min_res = num_unconcealed
            result = e
        elif num_unconcealed == min_res:
            result += e
    print("The result is: {0}".format(result))
