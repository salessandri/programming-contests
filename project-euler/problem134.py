#!/usr/bin/env python3

from CommonFunctions import find_primes_less_than
from itertools import takewhile, count, dropwhile

primes = find_primes_less_than(1100000)

limit = 10 ** 6
result = 0

dict = {}

for i in range(10):
    dict[i] = {}
    for j in range(10):
        dict[i][(i * j) % 10] = j

def better_finder(p1, p2):
    n = []
    carry = 0
    list_adders = []
    str_p1 = str(p1)
    str_p2 = str(p2)
    for i in range(1, len(str_p1) + 1):
        s = sum(int(s[-i]) for s in list_adders if len(s) >= i)
        to_find = (int(str_p1[-i]) - s - carry) % 10
        mult = dict[int(str_p2[-1])][to_find]
        n.append(str(mult))
        list_adders.append(str(mult * p2 * (10 ** (i - 1))))
        carry = (carry + s) // 10
    n = int(''.join(reversed(n)))
    return n * p2
    

if __name__ == '__main__':
    result = sum(better_finder(*t) for t in takewhile(lambda p: p[0] <= limit, ((primes[i], primes[i + 1]) for i in count(2))))
    print("The result is:", result)
