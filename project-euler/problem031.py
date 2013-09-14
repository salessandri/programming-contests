#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 31 from projectEuler.net.
#   Finds all the different ways of making £2 in english currency.
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
    amounts = [0 for x in range(201)]
    notes = [1, 2, 5, 10, 20, 50, 100, 200]
    for note in notes:
        amounts[note] += 1
        index = note + 1
        while index < len(amounts):
            amounts[index] += amounts[index - note]
            index += 1
    print("The result is:", amounts[200])
