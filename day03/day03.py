print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数

print('---------------------------')

print(123.456)    # 数学写法
print(1.23456e2)  # 科学计数法

print('---------------------------')

'''
使用变量保存数据并进行加减乘除运算

Version: 1.0
'''
a = 45        # 定义变量a，赋值45
b = 12        # 定义变量b，赋值12
print(a + b)   # 加法
print(a - b)   # 减法
print(a * b)   # 乘法
print(a / b)   # 除法
print(a // b)  # 整除
print(a % b)   # 取余
print(a ** b)  # 乘方

print('---------------------------')

"""
使用type函数检查变量的类型

Version: 1.0
"""
a = 100
b = 123.45
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

print('---------------------------')

"""
变量的类型转换操作

Version: 1.0
"""
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))  # 100.0
print(int(b))    # 123
print(int(c))    # 123
print(float(d))  # 100.0
print(float(e))  # 123.45
print(bool(f))   # True
print(bool(g))   # True
print(int(c, base=8))  # 83
print(int(c, base=16)) # 291
