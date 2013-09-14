#!/usr/bin/python3

########################################################################
#   Solves problem 172 from projectEuler.net.
#   Calculates the number of numbers of 18 digits that no digit is
#   repeated more than 3 times.
#   Copyright (C) 2011  Santiago Alessandri
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

dp_table = {
    (1, 5) : 5,
    (1, 4) : 6,
    (1, 3) : 7,
    (1, 2) : 8,
    (1, 1) : 9,
    (1, 0) : 10,
}

def solve(*args):
    if args in dp_table:
        return dp_table[args]
    if args[0] == 1:
        return dp_table[args[:2]]
    result = 0
    cant = 10 - args[1]
    if args[2]:
        result += args[2] * solve(args[0] - 1, args[1] + 1, args[2] - 1, args[3])
        cant -= args[2]
    if args[3]:
        result += args[3] * solve(args[0] - 1, args[1], args[2] + 1, args[3] - 1)
        cant -= args[3]
    if cant:
        result += cant * solve(args[0] - 1, args[1], args[2], args[3] + 1)
    dp_table[args] = result
    return result

if __name__ == '__main__':
    length = 17
    result = 9 * solve(length, 0, 0, 1)
    print("The result is:", result)
