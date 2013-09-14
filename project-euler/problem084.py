#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 84 from projectEuler.net.
#   Finds the 3 squares in Monopoly with more probabbility of ending
#   in them.
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

import random

board = [0 for x in range(40)]
cc = 0
ch = 0
doubles = 0
position = 0
rw = (5, 15, 25, 35)
ut = (12, 28)

def make_move():
    global board, cc, ch, doubles, position, rw, ut
    dice1 = random.randint(1, 4)
    dice2 = random.randint(1, 4)
    if dice1 == dice2:
        doubles += 1
    else:
        doubles = 0
    if doubles == 3:
        position = 10
        doubles = 0
        return
    position += dice1 + dice2
    position %= 40
    if position == 30:
        position = 10
        return
    elif position == 2 or position == 17 or position == 33:
        cc = (cc + 1) % 15
        if cc == 0:
            position = 0
            return
        elif cc == 1:
            position = 10
            return
    elif position == 7 or position == 22 or position == 36:
        ch = (ch + 1) % 15
        if ch == 0:
            position = 0
            return
        elif ch == 1:
            position = 10
            return
        elif ch == 2:
            position = 11
            return
        elif ch == 3:
            position = 24
            return
        elif ch == 4:
            position = 39
            return
        elif ch == 5:
            position = 5
            return
        elif ch == 6 or ch == 7:
            while position not in rw:
                position += 1
                if position == 40:
                    position = 0
            return
        elif ch == 8:
            while position not in ut:
                position += 1
                if position == 40:
                    position = 0
            return
        elif ch == 9:
            position -= 3
            return

if __name__ == '__main__':
    result = ""
    for i in range(10 ** 6):
        make_move()
        board[position] += 1
    max_prob = sorted((-board[i], i) for i in range(len(board)))
    result = "%2d%2d%2d" % (max_prob[0][1], max_prob[1][1], max_prob[2][1])
    print("The result is:", result)
    