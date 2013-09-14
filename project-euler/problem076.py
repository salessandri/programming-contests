#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 76 from projectEuler.net.
#   Finds the number of different ways that 100 can be written as sum of
#   2 positive integers.
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
    ways = [0 for x in range(101)]
    ways[0] = 1
    for coin in reversed(range(1, 100)):
        for index in range(coin, 101):
            ways[index] += ways[index - coin]
    print("The result is:", ways[100])