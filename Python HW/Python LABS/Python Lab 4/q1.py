# Question 1
user_input = float(input("Enter a score: "))
grade = "Default grade"

if 80 <= user_input <= 100:
    grade = 'A'
if 70 <= user_input < 80:
    grade = 'B'
if 60 <= user_input < 70:
    grade = 'C'
if 50 <= user_input < 60:
    grade = 'D'
if user_input < 50:
    grade = 'F'

print(grade)
