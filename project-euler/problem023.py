#!/usr/bin/env python3

########################################################################
#   Solves problem 23 from projectEuler.net.
#   Finds the sum of the numbers which aren't the sum of to abundant
#   numbers.
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

from CommonFunctions import factors

def is_abundant(n):
    lst = factors(n)
    lst.remove(n)
    if sum(lst) > n:
        return True
    return False


def is_sum_of_abundants(n, all_abundants, set_all_abundants):
    i = 0
    while all_abundants[i] <= n // 2:
        if (n - all_abundants[i] in set_all_abundants):
            return True
        i += 1
    return False

if __name__ == '__main__':
    all_abundants = [i for i in range(12, 28124) if is_abundant(i)]
    set_all_abundants = set(all_abundants)
    result = sum(i for i in range(1, 28124) if not is_sum_of_abundants(i, all_abundants, set_all_abundants))
    print("The result is:", result)
