#!/usr/bin/python

from fractions import Fraction

def solve():
    n, pd, pg = map(int, raw_input().split())
    if pg == 0 and pd > 0:
        return 'Broken'
    if pd == 0:
        return 'Possible'
    
    m_pd = Fraction(100, pd)
    if m_pd.numerator > n:
        return 'Broken'
    m_pg = Fraction(100, pg)
    if m_pg.numerator < m_pd.numerator:
        return 'Broken'
    return 'Possible'

if __name__ == '__main__':
    T = int(raw_input())
    for case in range(1, T+1):
        print "Case #{0}: {1}".format(case, solve())
