"""
BMI计算器

Version: 1.0
# """
height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
# if 18.5 <= bmi < 24:
#     print('你的身材很棒！')
# else:
#     print('你的身材不够标准哟！')

if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')


print('---------------------------')

status_code = int(input('响应状态码: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('状态码描述:', description)

print('---------------------------')

status_code = int(input('响应状态码: '))
match status_code:
    case 400:
        description = 'Bad Request'
    case 401:
        description = 'Unauthorized'
    case 403:
        description = 'Forbidden'
    case 404:
        description = 'Not Found'
    case 405:
        description = 'Method Not Allowed'
    case 418:
        description = 'I am a teapot'
    case 429:
        description = 'Too many requests'
    case _:
        description = 'Unknown status Code'
print('状态码描述:', description)


print('---------------------------')


status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)