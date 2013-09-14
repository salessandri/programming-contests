#!/usr/bin/env python3

########################################################################
#   Solves problem 90 from projectEuler.net.
#   Finds number of arrangements of 2 cubes so that they form all squares
#   below 100.
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
#   You can contact me at san.lt.ss@gmail.com or salessandri@nasel.com
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

from itertools import combinations

if __name__ == '__main__':
    result = 0
    for dice1 in combinations(range(10), 6):
        for dice2 in combinations(range(10), 6):
            if dice2 < dice1:
                continue
            if not ((0 in dice1 and 1 in dice2) or (0 in dice2 and 1 in dice1)):
                continue
            if not ((0 in dice1 and 4 in dice2) or (0 in dice2 and 4 in dice1)):
                continue
            if not ((0 in dice1 and 9 in dice2) or (0 in dice2 and 9 in dice1)) \
            and not ((0 in dice1 and 6 in dice2) or (0 in dice2 and 6 in dice1)):
                continue
            if not ((1 in dice1 and 6 in dice2) or (1 in dice2 and 6 in dice1)) \
            and not ((1 in dice1 and 9 in dice2) or (1 in dice2 and 9 in dice1)):
                continue
            if not ((2 in dice1 and 5 in dice2) or (2 in dice2 and 5 in dice1)):
                continue
            if not ((3 in dice1 and 6 in dice2) or (3 in dice2 and 6 in dice1)) \
            and not ((3 in dice1 and 9 in dice2) or (3 in dice2 and 9 in dice1)):
                continue
            if not ((4 in dice1 and 6 in dice2) or (4 in dice2 and 6 in dice1)) \
            and not ((4 in dice1 and 9 in dice2) or (4 in dice2 and 9 in dice1)):
                continue
            if not ((6 in dice1 and 4 in dice2) or (6 in dice2 and 4 in dice1)) \
            and not ((9 in dice1 and 4 in dice2) or (9 in dice2 and 4 in dice1)):
                continue
            if not ((8 in dice1 and 1 in dice2) or (8 in dice2 and 1 in dice1)):
                continue
            result += 1
    print("The result is:", result)
