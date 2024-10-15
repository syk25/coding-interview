grade = input()

if grade == "F":
    print(0.0)
else:
    score = ord("E") - ord(grade[0])

    small_grade = grade[1]
    if small_grade == '+':
        score += 0.3
    if small_grade == '0':
        score += 0.0
    if small_grade == '-':
        score -= 0.3
    print(score)
