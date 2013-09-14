#!/usr/bin/env python3

########################################################################
#   Solves problem 19 from projectEuler.net.
#   Finds the number of Sundays that were first of the month during
#   the 20th century.
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

import datetime

if __name__ == '__main__':
    result = 0
    for year in range(1901, 2001):
        for month in range(1,13):
            d = datetime.date(year, month, 1)
            if d.weekday() == 6:
                result += 1
    print("The result is:", result)
