#!/usr/bin/env python3

########################################################################
#   Solves problem 323 from projectEuler.net.
#   Calculates the average number of tries you need to get the 32 bits
#   in 1 using or operations with random numbers.
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
#   Visit my wiki at http://wiki.san-ss.com.ar
#   Visit my blog at http://blog.san-ss.com.ar
########################################################################

factorial = {0:1}
for i in range(1, 33):
    factorial[i] = factorial[i-1] * i

bits = 32

comb = lambda n, k: factorial[n] // (factorial[k] * factorial[n-k])

dp = {
    (0, 0) : 1
}

def get_value(*args):
    if args in dp:
        return dp[args]
    
    length, rem = args
    if length > 0 and rem == 0:
        return 0
    if length == 0 and rem > 0:
        return 0
    result = 0
    for i in range(bits+1):
        for overlooked in range(max(0, i-rem), min(i, bits-rem)+1):
            result += get_value(length-1, rem-i+overlooked) * ((comb(bits-rem, overlooked) * comb(rem, i-overlooked) / (2 ** bits)))
    
    dp[args] = result
    return result

iters = 50

if __name__ == '__main__':
    result = 0
    for i in range(1, iters+1):
        result += get_value(i, bits) * i
    print("The result is:", result)
