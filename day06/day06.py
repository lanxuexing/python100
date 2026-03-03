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
