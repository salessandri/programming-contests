#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 42 from projectEuler.net.
#   Finds the number of words which have a triangular value.
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

alphabetical_value = lambda name: sum(ord(c) - 64 for c in name)

if __name__ == '__main__':    
    f = open('words.txt', 'r')
    s = f.readline()
    f.close()
    lst = s.replace("\"", "").split(",")

    triangles = set(n * (n + 1) // 2 for n in range(1,1000))
    result = sum(1 for name in lst if alphabetical_value(name) in triangles)
    print("The result is:", result)