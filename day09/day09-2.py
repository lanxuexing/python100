"""
双色球随机选号程序
“虚构一个不劳而获的人，去忽悠一群想不劳而获的人，最终养活一批真正不劳而获的人”

Version: 1.0
"""
import random

red_balls = list(range(1, 34))
selected_balls = []
# 添加6个红色球到选中列表
for _ in range(6):
    # 生成随机整数代表选中的红色球的索引位置
    index = random.randrange(len(red_balls))
    # 将选中的球从红色球列表中移除并添加到选中列表
    selected_balls.append(red_balls.pop(index))
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 随机选择1个蓝色球
blue_ball = random.randrange(1, 17)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')


print('---------------------------')

"""
双色球随机选号程序

Version: 1.1
"""
import random

red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
# 从红色球列表中随机抽出6个红色球（无放回抽样）
selected_balls = random.sample(red_balls, 6)
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 从蓝色球列表中随机抽出1个蓝色球
blue_ball = random.choice(blue_balls)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')


print('---------------------------')

"""
双色球随机选号程序

"""
import random

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
for _ in range(n):
    # 从红色球列表中随机抽出6个红色球（无放回抽样）
    selected_balls = random.sample(red_balls, 6)
    # 对选中的红色球排序
    selected_balls.sort()
    # 输出选中的红色球
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    # 从蓝色球列表中随机抽出1个蓝色球
    blue_ball = random.choice(blue_balls)
    # 输出选中的蓝色球
    print(f'\033[034m{blue_ball:0>2d}\033[0m')


print('---------------------------')

"""
双色球随机选号程序

# 导入包里的子模块
from package import module

# 导入多个内容
from rich import Console, Table, Panel

# 相对导入（包内部）
from .sibling import something
from ..parent import other

# 条件导入（兼容不同版本）
try:
    import json
except ImportError:
    import simplejson as json
"""
import random

from rich.console import Console
from rich.table import Table


# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)