
if __name__ == '__main__':
    tc = int(raw_input())
    for i in xrange(tc):
        a, b = map(int, raw_input().split(' '))
        a %= 10
        b = b > 0 and (b % 4 or 4) or 0
        print (a ** b) % 10
