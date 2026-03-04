"""
每隔1s输出一次"hello, world"，共输出5次
"""
# import time

# for _ in range(5):
#     print('hello, world')
#     time.sleep(1)


print('---------------------------')

"""
从1-100的整数求和

Version: 1.0
"""
total = 0
for x in range(1, 101):
    total += x
print(f'1-100的整数和: {total}')


print('---------------------------')

"""
从1到100的偶数求和
"""
total = 0
# for x in range(2, 101, 2):
#     total += x

for x in range(1, 101):
    if x % 2 == 0:
        total += x
print(f'1-100的偶数和: {total}')


print('---------------------------')

"""
从1-100的奇数求和

Vseion: 1.0
"""
print(f'1-100的奇数和: {sum(range(1, 101, 2))}')

print('---------------------------')

"""
从1到100的整数求和

Vseion: 1.0
"""
total = 0
i = 1
while i < 101:
    total += i
    i += 1
print(f'1-100的整数和: {total}')


print('---------------------------')

"""
打印乘法口诀表

Version: 1.0
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()