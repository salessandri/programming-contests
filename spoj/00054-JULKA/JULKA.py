#!/usr/bin/python

if __name__ == '__main__':
    for i in xrange(10):
        total = int(raw_input())
        diff = int(raw_input())
        if diff & 1:
            diff += 1
        max = total / 2 + diff / 2
        min = total - max
        print max
        print min
