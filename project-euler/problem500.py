#!/usr/bin/env python3

########################################################################
#   Solves problem 500 from projectEuler.net.
#   Calculates the probability of a series of croaks.
#   Copyright (C) 2020  Santiago Alessandri
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
########################################################################

import functools
import heapq

MODULI = 500500507

primes = []
with open('primes1.txt') as f:
    primes = [int(prime_str) for line in f.readlines() for prime_str in line.split()]

def calculate(pow_2):
    available_prime_pows = primes
    heapq.heapify(available_prime_pows)
    prime_composed = []
    while len(prime_composed) < pow_2:
        to_use = heapq.heappop(available_prime_pows)
        prime_composed.append(to_use)
        heapq.heappush(available_prime_pows, to_use ** 2)

    result = functools.reduce(lambda x,y: ((x % MODULI) * (y % MODULI)) % MODULI, prime_composed, 1)
    return result

if __name__ == '__main__':
    result = calculate(500500)
    print("The result is: {}".format(result))
