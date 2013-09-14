#!/usr/bin/python3

from CommonFunctions import find_primes_less_than

numbers = {
    '1' : {1, 2},
    '2' : {0, 1, 3, 4, 6},
    '3' : {0, 1, 2, 3, 6},
    '4' : {1, 2, 5, 6},
    '5' : {0, 2, 3, 5, 6},
    '6' : {0, 2, 3, 4, 5, 6},
    '7' : {0, 1, 2, 5},
    '8' : {0, 1, 2, 3, 4, 5, 6, 7},
    '9' : {0, 1, 2, 3, 5, 6, 7},
    '0' : {0, 1, 2, 3, 4, 5, 6},
    'x' : set()
    }

def sam_clock(n):
    global numbers
    result = 0
    while n >= 10:
        result += sum(len(numbers[c]) for c in str(n)) * 2
        n = sum(int(c) for c in str(n))
    result += sum(len(numbers[c]) for c in str(n)) * 2
    return result

def max_clock(n):
    global numbers
    result = 0
    prev_n = 'x' * len(str(n))
    while n >= 10:
        str_n = 'x' * (len(prev_n) - len(str(n))) + str(n)
        result += sum(len((numbers[a] | numbers[b]) - (numbers[a] & numbers[b])) for a,b in zip(prev_n, str_n))
        prev_n = str(n)
        n = sum(int(c) for c in str(n))
    str_n = 'x' * (len(prev_n) - len(str(n))) + str(n)
    result += sum(len((numbers[a] | numbers[b]) - (numbers[a] & numbers[b])) for a,b in zip(prev_n, str_n))
    result += sum(len(numbers[a]) for a in str(n))
    return result

if __name__ == '__main__':
    primes = (x for x in find_primes_less_than(2 * (10 ** 7)) if x > 10 ** 7)
    result = sum(sam_clock(x) - max_clock(x) for x in primes)
    print("The result is: {0}", result)
