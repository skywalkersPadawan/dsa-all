if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = [score for name, score in students]
    second_lowest = sorted(set(scores))[1]
    names = sorted(
        [name for name, score in students if score == second_lowest])
    for name in names:
        print(name)

'''
scores = [score for name, score in students]

for this the equivalent normal code is:

scores = []
for name, score in students:
  scores.append(score)
'''
