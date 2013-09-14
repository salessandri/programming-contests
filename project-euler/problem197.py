#!/usr/bin/env python3

########################################################################
#   Solves problem 197 from projectEuler.net.
#   Finds the sum of 2 values of a recursively defined sequence.
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
#   Visit my wiki at http://san-ss.is-a-geek.com.ar
########################################################################

f_x = lambda x: int(2 ** (30.403243784 - x ** 2)) * (10 ** -9)

if __name__ == '__main__':
    x_1 = -1
    for i in range(1000):
        x_2 = f_x(x_1)
        x_1 = f_x(x_2)
    print("The result is:", x_1 + x_2)
