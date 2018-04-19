#!/usr/bin/python


def next_palindrome(n):
    if min(n) == '9':
        n = str(int(n) + 1)
    list_n = list(n)
    start = 0
    end = len(list_n) - 1
    while start < end:
        if list_n[start] < list_n[end]:
            list_n[end] = list_n[start]
            j = end - 1
            while list_n[j] == '9':
                list_n[j] = '0'
                j -= 1
            list_n[j] = str(int(list_n[j]) + 1)
            
            if j <= start:
                start = j
                end = len(list_n) - j - 1
                continue
        elif list_n[start] > list_n[end]:
            list_n[end] = list_n[start]
        start += 1
        end -= 1
    new_n = ''.join(list_n)
    if n == new_n:
        return next_palindrome(str(int(new_n) + 1))
    return new_n

if __name__ == '__main__':
    tc = int(raw_input())
    for i in xrange(tc):
        n = raw_input()
        print next_palindrome(n)

