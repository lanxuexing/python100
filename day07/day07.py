"""
输出100以内的素数

Version: 1.0
"""
for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
print()

print('---------------------------')

"""
输出斐波那契数列中的前20个数

Version: 1.0
"""
a, b = 0, 1
for _ in range(20):
    print(a, end=' ')
    a, b = b, a + b
print()