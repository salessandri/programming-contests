#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
#   Solves problem 51 from projectEuler.net.
#   Finds the first subset of 8 primes that share a "mask".
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

from itertools import permutations, takewhile
from CommonFunctions import find_primes_less_than

def build_masks(n):
    masks = set()
    for i in range(1, n):
        zeros = [0 for x in range(n-i)]
        ones = [1 for x in range(i)]
        for mask in permutations(zeros + ones):
            masks.add(mask)
    return masks

def apply_mask(n, mask):
    str_n = str(n)
    result = ""
    remain = ""
    for i in range(len(mask)):
        result += mask[i] and str_n[i] or ""
        remain += (not mask[i]) and str_n[i] or ""
    return result, int(remain)
    
if __name__ == '__main__':

    primes = find_primes_less_than(1000000)
    length = 0
    result = None
    for prime in takewhile(lambda x: result is None, primes):
        if len(str(prime)) > length:
            length = len(str(prime))
            masks = build_masks(length)
            groups = {}
        for mask in masks:
            res, remain = apply_mask(prime, mask)
            if min(res) == max(res):
                if mask not in groups:
                    groups[mask] = {}
                if remain not in groups[mask]:
                    groups[mask][remain] = []
                groups[mask][remain].append(prime)
                if len(groups[mask][remain]) == 8:
                    result = min(groups[mask][remain])
                    break
    print("The result is:", result)
