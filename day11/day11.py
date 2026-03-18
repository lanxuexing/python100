# import requests
# import re
# import time

# local = time.strftime("%Y.%m.%d")
# url = 'https://www.bing.com/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
# con = requests.get(url, headers=headers)
# content = con.text

# # 提取图片 URL - 获取 1920x1200 高清版本
# reg = r'th\?id=(OHR[^"\&]+)_1920x1200\.jpg'
# match = re.search(reg, content)
# if match:
#     ohr_id = match.group(1)
#     picUrl = f'https://www.bing.com/th?id={ohr_id}_1920x1200.jpg'
#     print(f'Bing image: {picUrl}')

#     read = requests.get(picUrl, headers=headers)
#     with open(f'{local}.jpg', 'wb') as f:
#         f.write(read.content)
#     print(f'Saved to {local}.jpg')
# else:
#     print('Failed to extract Bing image URL')



s1 = 'hello, world!'
s2 = "你好，世界！❤️"
s3 = '''hello,
wonderful
world!'''
print(s1)
print(s2)
print(s3)


print('---------------------------')

s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)


print('---------------------------')

s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!

print('---------------------------')

print('H的Unicode编码是：', ord('H'))  # 72
print('Unicode编码为72的字符是：', chr(72))  # H


print('---------------------------')

s = 'abc123456'
n = len(s)
print(s[0], s[-n])    # a a
print(s[n-1], s[-1])  # 6 6
print(s[2], s[-7])    # c c
print(s[5], s[-4])    # 3 3
print(s[2:5])         # c12
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba

print('---------------------------')

s = 'hello'
for i in range(len(s)):
    print(s[i])

print('---------------------------')

s = 'hello world'
print(s.capitalize())  # Hello world
print(s.title())       # Hello World
print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.swapcase())    # HELLO WORLD


print('---------------------------')

s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
# print(s.index('or', 9))  # ValueError: substring not found

print('---------------------------')

s2 = 'abc123456'
print(s2.isalnum())  # True
print(s2.isalpha())  # False
print(s2.isdigit())  # False
print(s2.islower())  # True
print(s2.isupper())  # False
print(s2.isspace())  # False


print('---------------------------')

s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界