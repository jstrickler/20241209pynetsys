scores = {}
total_of_scores = 0

with open("../DATA/testscores.dat") as f:
    for line in f:
        (name, score) = line.split(":")
        score = int(score)
        scores[name] = score
        total_of_scores += score

for student, score in sorted(scores.items(), key=lambda e: (e[1]),
                             reverse=True):
    grade = None
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    print(f"{student:20s} {score} {grade}")

average = total_of_scores / len(scores)
print(f"\naverage score is  {average:.2f}\n")
