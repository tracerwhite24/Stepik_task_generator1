def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

genny = fibonacci(n=10)
print(genny)

for value in genny:
    print(value)

