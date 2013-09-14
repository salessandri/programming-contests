#!/usr/bin/env python3

def get_factorisation(n, k):
    r = {}
    not_p = set()
    tope_1 = min(n-k, k) + 1
    tope_2 = max(n-k, k) + 1
    for i in range(2, n+1):
        if i not in not_p:
            if i < tope_1:
                r[i] = -i
            elif i < tope_2:
                r[i] = 0
            else:
                r[i] = i
            for j in range(i*2, n+1, i):
                not_p.add(j)
                if j < tope_1:
                    mult = -1
                elif j >= tope_2:
                    mult = 1
                else:
                    continue
                cant = 0
                d, rest = divmod(j, i)
                while not rest:
                    cant += 1
                    d, rest = divmod(d, i)
                r[i] += mult * cant * i
            if r[i] == 0:
                del r[i]
    return r


if __name__ == '__main__':
    fact = get_factorisation(20000000, 15000000)
    print("Result is:", sum(i for i in fact.items()))