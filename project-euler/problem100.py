#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 100 from projectEuler.net.
#   Finds the first arrangement to contain over 10**12 discs, so that 
#   the chance of taking 2 blue disks is 0.5.
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

# Intro:
# (b / n) * ((b - 1) / (n - 1)) = 1 / 2
# (b * (b - 1)) / (n * (n - 1)) = 1 / 2
# (b^2 - b) / (n^2 - n) = 1 / 2
# 2(b^2 - b) / (n^2 - n) = 1
# 2(b^2 - b) = n^2 - n
# 2b^2 - 2b - n^2 + n = 0 <- Quadratic diophantine equation
#
# Using http://www.alpertron.com.ar/QUAD.HTM, using b as X and n as Y.
# We get that we have that the series is found by:
#
# X_0 = 1 and Y_0 = 1
# X_n+1 = P * X_n + Q * Y_n + K
# Y_n+1 = R * X_n + S * Y_n + L
#
# Having:
# P = 3, Q = 2, K = -2, R = 4, S = 3, L = -3
 
if __name__ == '__main__':
    p = 3
    q = 2
    k = -2
    r = 4
    s = 3
    l = -3
    
    b = 15
    n = 21
    while n < 10 ** 12:
        b, n = (p * b + q * n + k, r * b + s * n + l)
    print("The result is:", b)
