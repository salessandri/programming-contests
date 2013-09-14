
if __name__ == '__main__':
    tc = int(raw_input())
    for i in xrange(tc):
        raw_input()
        a, result = raw_input().split(' + ')
        b, result = result.split(' = ')
        if 'machula' in a:
            a = str(int(result) - int(b))
        elif 'machula' in b:
            b = str(int(result) - int(a))
        elif 'machula' in result:
            result = str(int(a) + int(b))
        print "%s + %s = %s" % (a, b, result)
