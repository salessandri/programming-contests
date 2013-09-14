#!/usr/bin/env python3

########################################################################
#   Solves problem 15 from projectEuler.net.
#   Finds the number of routes in a 20x20 sided square.
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
    #Building the matrix
    sqre = [[]]
    for i in range(21):
        sqre[0].append(1)
    for i in range(1,21):
        row = [1]
        for i in range(1,21):
            row.append(0)
        sqre.append(row)
    #Processing the routes
    for i in range(1,21):
        for j in range(1, 21):
            sqre[i][j] = sqre[i-1][j] + sqre[i][j-1]
    print("The result is:", sqre[20][20])


