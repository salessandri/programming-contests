#!/usr/bin/env python3

########################################################################
#   Solves problem 109 from projectEuler.net.
#   Counts how many distinct ways can a player checkout with a score 
#   less than 100 in a game of darts.
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

limit = 100

doubles = set(2 * x for x in range(1, 21))
doubles.add(50)
casual = sorted([x for x in range(1,21)] + [2 * x for x in range(1, 21)] + [3 * x for x in range(1, 21)] + [25] + [50])

if __name__ == '__main__':
    result = 0
    for score in range(2, limit):
        if score in doubles:
            result += 1
        for first in casual:
            if first >= score:
                break
            result += (score - first) in doubles and 1 or 0
        first = 0
        while first < len(casual) and casual[first] * 2 < score:
            remain = score - casual[first]
            second = first
            while second < len(casual) and casual[second] < remain:
                result += (remain - casual[second]) in doubles and 1 or 0
                second += 1
            first += 1
    print("The result is:", result)
