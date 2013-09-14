#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 55 from projectEuler.net.
#   Finds the amount of Lychrel numbers below 10000
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

from CommonFunctions import is_palindrome

def is_lychrel(n):
    count = 1
    n = n + int(''.join(reversed(str(n))))
    while count < 50:
        if is_palindrome(n):
            return False
        n = n + int(''.join(reversed(str(n))))
        count += 1
    return True

if __name__ == '__main__':
    result = sum(1 for i in range(10, 10001) if is_lychrel(i))
    print("The result is:", result)
