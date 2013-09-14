
from CommonFunctions import find_primes_less_than
from itertools import combinations

LIMIT = 120000

primes = find_primes_less_than(LIMIT)

p_to_n = {}
factors = [[set(), 1] for i in range(LIMIT)]
for p in primes:
    p_to_n[p] = set()
    for i in range(p, LIMIT, p):
        p_to_n[p].add(i)
        factors[i][0].add(p)
        factors[i][1] *= p

result = 0
for b in range(2, LIMIT - 1):
    possibles_a = set(range(1, min(LIMIT - b, b)))
    possibles_a.difference_update(*(p_to_n[p] for p in factors[b][0]))
    for a in possibles_a:
        c = a + b
        if factors[a][1] * factors[b][1] * factors[c][1] < c:
            result += c
print("Result:", result)
#~ 
#~ result = 0
#~ for c in range(3, LIMIT):
    #~ for a, b in ((a, c - a) for a in range(1, c // 2 + 1)):
        #~ if (factors[a][0] & factors[b][0]):
           #~ continue 
        #~ if factors[a][1] * factors[b][1] * factors[c][1] < c:
            #~ print("Found:", (a, b, c), "->", factors[a][1] * factors[b][1] * factors[c][1])
            #~ result += c
            #~ 
#~ print("Result:", result)
            #~ 
