#!/usr/bin/python

def solve_sum(str_n, str_m):
    n = int(str_n)
    m = int(str_m)
    result = n + m
    str_res = str(result)
    str_m = "+" + str_m
    width = max(len(str_n), len(str_m), len(str_res))
    dash_width = max(len(str_m), len(str_res))
    print " " * (width - len(str_n)) + str_n
    print " " * (width - len(str_m)) + str_m
    print " " * (width - dash_width) + "-" * dash_width
    print " " * (width - len(str_res)) + str_res

def solve_subs(str_n, str_m):
    n = int(str_n)
    m = int(str_m)
    result = n - m
    str_res = str(result)
    str_m = "-" + str_m
    width = max(len(str_n), len(str_m), len(str_res))
    dash_width = max(len(str_m), len(str_res))
    print " " * (width - len(str_n)) + str_n
    print " " * (width - len(str_m)) + str_m
    print " " * (width - dash_width) + "-" * dash_width
    print " " * (width - len(str_res)) + str_res

def solve_mul(str_n, str_m):
    n = int(str_n)
    width = len(str_n)
    res = 0
    str_mid = []
    digits = list(str_m)
    digits.reverse()
    for dig in digits:
        tmp = int(dig) * n
        res += tmp * (10 ** len(str_mid)) 
        str_mid.append(str(tmp) + " " * len(str_mid))
        width = max(width, len(str_mid[-1]))
    str_res = str(res)
    str_m = '*' + str_m
    width = max(width, len(str_m), len(str_res))
    dash_width = max(len(str_m), len(str_mid[0]))
    print ' ' * (width - len(str_n)) + str_n
    print ' ' * (width - len(str_m)) + str_m
    print ' ' * (width - dash_width) + '-' * dash_width
    if len(str_m) > 2:
        for mid in str_mid:
            tmp_width = width - len(mid)
            print ' ' * tmp_width + mid.strip()
        dash_width = max(len(str_res), len(str_mid[-1]))
        print ' ' * (width - dash_width) + '-' * dash_width
    print ' ' * (width - len(str_res)) + str_res

if __name__ == '__main__':
    tc = int(raw_input())
    for i in xrange(tc):
        line = raw_input()
        if '+' in line:
            str_n, str_m = line.split('+')
            solve_sum(str_n, str_m)
        elif '-' in line:
            str_n, str_m = line.split('-')
            solve_subs(str_n, str_m)
        else:
            str_n, str_m = line.split('*')
            solve_mul(str_n, str_m)
        print ""
