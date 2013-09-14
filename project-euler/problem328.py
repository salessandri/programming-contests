dp = {
}

def indexes(i, base):
    if i <= 0:
        return 0
    if i == 1:
        return 0
    if i == 2:
        return base
    if (i, base) in dp:
        return dp[(i, base)]
    
    minim = 10 ** 9
    for j in range(i):
        left_to_j = indexes(j, base) + (j + base)
        right_to_j = (j + base) + indexes(i - j - 1, base + j + 1)
        final_tmp = left_to_j > right_to_j and left_to_j or right_to_j
        if final_tmp < minim:
            minim = final_tmp
    
    dp[(i, base)] = minim
    return minim

res = 0
for k in range(1, 200001):
    print(k)
    res += indexes(k, 1)
