"""
将华氏温度转换为摄氏温度

Version: 1.0
"""
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
# print('%d华氏度 = %.1f摄氏度' % (f, c))
# print(f'{f}华氏度 = {c}摄氏度')


"""
输入半径计算圆的周长和面积

Version: 1.1
"""
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')
