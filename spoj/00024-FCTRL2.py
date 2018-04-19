#!/usr/bin/python

fact = {0:1}
tmp = 1

for i in xrange(1,101):
    fact[i] = tmp = tmp * i

if __name__ == '__main__':
    tc = int(raw_input())
    for i in xrange(tc):
        print fact[int(raw_input())]

