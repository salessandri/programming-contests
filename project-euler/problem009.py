#!/usr/bin/env python3

########################################################################
#   Solves problem 9 from projectEuler.net.
#   Finds the pitagorean triangle with perimeter 1000 and returns the
#   product of the sides.
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
    a = 1
    b = 1
    c = 1
    for a in range(1, 998):
        for b in range(a, 998):
            c = 1000 - b - a
            if (a ** 2 + b ** 2) == c ** 2:
                break
        if (a ** 2 + b ** 2) == c ** 2:
            break
    print("The result is:", a * b * c)


