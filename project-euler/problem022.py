#!/usr/bin/env python3

########################################################################
#   Solves problem 22 from projectEuler.net.
#   Finds the sum of the name's scores.
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

def alphabetical_value(name):
    result = 0
    for letter in name:
        result += ord(letter) - 64
    return result


if __name__ == '__main__':
    f = open('names.txt', 'r')
    s = f.readline()
    lst = s.replace("\"", "").split(",")
    lst.sort()
    result = 0
    for index in range(0, len(lst)):
        result += alphabetical_value(lst[index]) * (index + 1)
    print("The result is:", result)
