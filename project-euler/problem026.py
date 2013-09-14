#!/usr/bin/env python3

########################################################################
#   Solves problem 26 from projectEuler.net.
#   Finds the number below 1000 which has the longest cycle when 1/d.
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

def find_cycle_length(n):
    tmp = 1
    decimal = []
    digit = tmp / n
    module = tmp % n
    while (digit, module) not in decimal:
        decimal.append((digit, module))
        tmp = module * 10
        digit = tmp // n
        module = tmp % n
    while (digit, module) != decimal[0]:
        decimal.pop(0)
    return len(decimal)

if __name__ == '__main__':
    result = 0
    max_len = 0
    for d in range(2,1000):
        length = find_cycle_length(d)
        if length > max_len:
            result = d
            max_len = length
    print("The result is:", result)
