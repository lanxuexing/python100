"""
猜数字小游戏

Version: 1.0
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('猜小了')
    elif number > answer:
        print('猜大了')
    else:
        print(f'恭喜你，猜对了！答案就是{answer}。你总共猜了{counter}次。')
        break