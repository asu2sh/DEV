def rope_cut(n, a, b, c):
    if n == 0: return 0
    if n < 0: return -1
    
    res = max(rope_cut(n-a, a, b, c),
              rope_cut(n-b, a, b, c),
              rope_cut(n-c, a, b, c)) + 1

    if res == 0:
        return -1
    return res


n, a, b, c = int(input()), int(input()), int(input()), int(input())
print(rope_cut(n, a, b, c))
