#!/usr/bin/python

def sieve(n):
    prime_set = set()
    prime_list = [True] * (n + 1)
    for i in xrange(2, n + 1):
        if not prime_list[i]:
            continue
        prime_set.add(i)
        for j in xrange(i * 2, n+1, i):
            prime_list[j] = False
    
    return prime_set

def sieve_from_to(from_, to_, prime_set):
    result_list = []
    prime_list = [True] * (to_ - from_ + 1)
    for prime in prime_set:
        if to_ < prime:
            continue
        i = 0
        if from_ % prime != 0:
            i = prime - (from_ % prime)
        if (i + from_) == prime:
            i += prime
        while i < len(prime_list):
            prime_list[i] = False
            i += prime
    for i in xrange(0, len(prime_list)):
        if prime_list[i]:
            result_list.append(i + from_)
    return result_list

if __name__ == '__main__':
    #Setup
    primes = sieve(32000)
    
    test_cases = int(raw_input())
    for i in range(test_cases):
        low, top = map(int, raw_input().split(' '))
        while low < 2:
            low += 1
        #~ if low & 1 == 0:
            #~ low += 1
        #~ if low <= 2:
            #~ print 2
        #~ for n in xrange(low, top+1, 2):
            #~ to_print = True
            #~ if n < 32000:
                #~ to_print = n in primes
            #~ else:
                #~ for j in primes:
                    #~ if n % j == 0:
                        #~ to_print = False
                        #~ break
            #~ if to_print:
                #~ print n
        for prime in sieve_from_to(low, top, primes):
            print prime
        if i < test_cases -1:
            print ""
