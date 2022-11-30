student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

scores = student_scores.copy()
for key, value in scores.items():
    if value >= 91:
        scores[key] = 'Outstanding'
    if value <= 90 and value >= 81:
        scores[key] = 'Exceeds Expectations'
    if value <= 80 and value >= 71:
        scores[key] = 'Acceptable'
    if value <= 70:
        scores[key] = 'Fail'
print(scores)


student_grades = {}


for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"