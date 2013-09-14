#!/usr/bin/env python3

########################################################################
#   Solves problem 158 from projectEuler.net.
#   Finds maximum number of combinations of strings that only have one
#   character bigger than the one to its left.
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
for i in range(1, 27):
    factorial[i] = factorial[i-1] * i

dp = {
    (0, 0, 0) : 0,
    (0, 0, 1) : 1
}
def get_num(*args):
    if args in dp:
        return dp[args]
    
    length, num_greater, count = args
    if count > 1:
        return 0
    result = sum(get_num(length-1, i, count + ((i < num_greater) and 1 or 0)) for i in range(length))
    dp[args] = result
    return result
        
p = lambda n: sum(get_num(n-1, i, 0) for i in range(n)) * (factorial[26] // (factorial[n] * factorial[26 - n]))

if __name__ == '__main__':
    max_pn, max_n = max((p(n), n) for n in range(2, 27))
    print("The result is:", max_pn, "found at n:", max_n)
