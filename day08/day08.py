items7 = ['Python', 'Java', 'JavaScript']
print(items7 * 2)

print('---------------------------')

items8 = ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
print(items8[-2:-6:-1])

print('---------------------------')

languages = ['Python', 'Java', 'C++', 'Kotlin']
for language in range(len(languages)):
    print(languages[language])

print('---------------------------')

languages = ['Python', 'Java', 'C++', 'Kotlin']
for language in languages:
    print(language)

print('---------------------------')


languages = ['Python', 'Java', 'C++', 'Kotlin']
for i, language in enumerate(languages):
    print(f"{i}: {language}")

"""
场景	推荐写法
只需要元素	for item in items
需要索引 + 元素	for i, item in enumerate(items)
只需要索引	for i in range(len(items))（较少见）
"""