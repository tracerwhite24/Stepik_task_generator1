def genny(n):
    for i in range (1, n + 1):
        if i % 2 == 0:
            yield i

print(list(genny(100)))
