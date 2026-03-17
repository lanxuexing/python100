languages = ['Python', 'Java', 'C++', 'Python']
languages.append('Kotlin')
print(languages)

print('---------------------------')

languages.insert(1, 'Go')
print(languages)

print('---------------------------')

# languages.remove('Python')
# print(languages)

print(languages.index('Python', 1))

print('---------------------------')

print(languages.count('Python'))

print('---------------------------')

items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

print('---------------------------')

# items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
# print(items)

items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

print('---------------------------')

"""
有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
[表达式 for 变量 in 可迭代对象]

[ 表达式     for 变量 in 可迭代对象     if 条件 ]
   ↑                ↑                      ↑
 结果要存什么    怎么循环              过滤条件（可选）


[x ** 2 if x % 2 == 0 else x for x in range(10)]

# 翻译成人话：
# "对于每个 x，偶数算平方，奇数保持不变"
# 每个数都会出现在结果里

for x in range(10):
    if x % 2 == 0:
        结果.append(x ** 2)  # 偶数平方
    else:
        结果.append(x)       # 奇数不变


"""
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)

print('---------------------------')
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)

