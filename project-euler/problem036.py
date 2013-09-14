#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 36 from projectEuler.net.
#   Finds the sum of the numbers below 1 millon which are both palindromic
#   in their decimal and binary representation.
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

if __name__ == '__main__':
    result = sum(x for x in range(1, 1000000, 2) if is_palindrome(x) and is_palindrome(bin(x)[2:]))
    print("The result is:", result)