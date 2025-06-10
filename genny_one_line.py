generator1 = (i for i in range(1, 100) if (i % 2 == 0) and (sum(int(digit) for digit in str(i)) != 8))

print(list(generator1))
