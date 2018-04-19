#!/usr/bin/python

coins = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    }

def solve(n):
    global coins
    
    if n in coins:
        return coins[n]
    else:
        coins[n] = result = max(n, solve(n/4) + solve(n/3) + solve(n/2))
        return result

if __name__ == '__main__':
    try:
        while True:
            n = int(raw_input())
            print solve(n)
    except EOFError:
        pass
    
