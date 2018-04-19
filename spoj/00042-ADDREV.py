#!/usr/bin/python

def reverse(n):
    l_n = list(str(n))
    l_n.reverse()
    return int(''.join(l_n))

if __name__ == '__main__':
    tc = int(raw_input())
    for i in xrange(tc):
        n, m = map(int, raw_input().split(' '))
        res = reverse(reverse(n) + reverse(m))
        print res
        
