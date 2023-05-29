from homework import Homework
from exam import Exam
from newgrade import ExamGrade

st = Homework()
st.grade = 95
assert st.grade == 95

print("______________________")

st1 = Exam()
st1.writing_grade = 88
st1.math_grade = 67

print(f'oceny -> writing: {st1.writing_grade}, math: {st1.math_grade}')
assert st1.writing_grade == 88
assert st1.math_grade == 67

print("______________________")

fe = ExamGrade()
fe.writing_grade = 54
fe.math_grade = 34
fe.science_grade = 13

print(f'oceny I termin  [EgamGrade] -> writing: {fe.writing_grade}, math: {fe.math_grade}, '
      f'science: {fe.science_grade}')

se = ExamGrade()
se.writing_grade = 77
se.math_grade = 88
se.science_grade = 99

print(f'oceny II termin [EgamGrade] -> writing: {se.writing_grade}, math: {se.math_grade}, '
      f'science: {se.science_grade}')

print("_przzypomnienie I termin: ")
print(f'oceny I termin - przypomnienie  [EgamGrade] -> writing: {fe.writing_grade}, math: {fe.math_grade}, '
      f'science: {fe.science_grade}')
