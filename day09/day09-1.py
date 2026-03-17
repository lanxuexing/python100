scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0])
print(scores[0][1])

print('---------------------------')

# scores = []
# for i in range(5):
#     score = []
#     for j in range(3):
#         score.append(int(input(f"请输入第{i + 1}个学生的第{j + 1}门课的成绩：")))
#     scores.append(score)
# print(scores)


print('---------------------------')
import random
scores = [[random.randint(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)