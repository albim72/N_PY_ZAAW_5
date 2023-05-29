st = Homework()
st.grade = 95
assert st.grade == 95

print("______________________")

st1 = Exam()
st1.writing_grade = 120
st1.math_grade = 67

print(f'oceny -> writing: {st1.writing_grade}, math: {st1.math_grade}')
assert st1.writing_grade == 88
assert st1.math_grade == 67
