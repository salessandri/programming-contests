#!/usr/bin/env python3

########################################################################
#   Solves problem 86 from projectEuler.net.
#   Finds the lowest M so that the sum of boxes with sides <= M exceeds
#   1000000.
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


if __name__ == '__main__':
    cant = 0
    limit = 10 ** 6
    m = 0
    while cant <= limit:
        m += 1
        m_sq = m ** 2
        for l23 in range(2, m*2 + 1):
            l23_sq = l23 ** 2
            side = m_sq + l23_sq
            sq = int(side**(.5))
            if sq**2 == side:
                to_sum = min(l23 // 2, int(m - l23 / 2) + 1)
                cant += to_sum
    print("The result is:", m)