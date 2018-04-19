
def choose(n,k):
    k = min(k,n-k)
    p = q = 1
    for i in xrange(k):
        p *= n - i
        q *= 1 + i
    return p/q

if __name__ == '__main__':
    tc = int(raw_input())
    for i in xrange(tc):
        n, k = map(int, raw_input().split())
        cookies = n - k
        print choose(cookies + k - 1, k-1)
