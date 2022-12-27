student_score = [78, 65, 89, 86, 55, 91, 64, 89]

max = 0
for score in student_score:
    if score > max:
        max = score

print(f"High score is {max}")