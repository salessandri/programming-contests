#!/usr/bin/python


if __name__ == '__main__':
    tc = int(raw_input())
    
    for i in xrange(tc):
        n = int(raw_input())
        div = 5
        result = 0
        while (div <= n):
            result += n / div 
            div *= 5
        print result
