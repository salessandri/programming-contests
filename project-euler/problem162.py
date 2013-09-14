#!/usr/bin/env python3

########################################################################
#   Solves problem 162 from projectEuler.net.
#   Finds the number of hexadecimal numbers of 16 digits or less that
#   have 0, 1 and A in them.
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

solved_dict = {
    (False, False, False, False, 1) : 0,
    (True, False, False, False, 1) : 0,
    (True, False, False, True, 1) : 0,
    (True, False, True, False, 1) : 0,
    (True, False, True, True, 1) : 1,
    (True, True, False, False, 1) : 0,
    (True, True, False, True, 1) : 1,
    (True, True, True, False, 1) : 1,
    (True, True, True, True, 1) : 16,
}

def solve(*args):
    if args in solved_dict:
        return solved_dict[args]
    result = 0
    if args[0] is False:
        result += solve(False, False, False, False, args[4] - 1)
        result += 13 * solve(True, False, False, False, args[4] - 1)
        result += solve(True, False, True, False, args[4] - 1)
        result += solve(True, False, False, True, args[4] - 1)
    else:
        result += 13 * solve(True, args[1], args[2], args[3], args[4] - 1)
        result += solve(True, True, args[2], args[3], args[4] - 1)
        result += solve(True, args[1], True, args[3], args[4] - 1)
        result += solve(True, args[1], args[2], True, args[4] - 1)
    solved_dict[args] = result
    return result

if __name__ == '__main__':
    print("The result is ", hex(solve(False, False, False, False, 16)).upper()[2:])