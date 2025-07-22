# Admission to a professional course is subject to the following conditions:

# Marks in mathematics >=60
# Marks in physics >=50
# Marks in chemistry >=40
# Total marks >=200 or total in mathematics and physics >=150

# Given the marks in three subjects, write a program to process the applications to list eligible
#candidates.

marks_math = float(input("Enter marks in Mathematics: "))
marks_physics = float(input("Enter marks in Physics: "))
marks_chemistry = float(input("Enter marks in Chemistry: "))


total_marks = marks_math + marks_physics + marks_chemistry
total_math_physics = marks_math + marks_physics

if ((marks_math >= 60 and marks_physics >= 50 and
    marks_chemistry >= 40 and total_marks >= 200) or total_math_physics >= 150):
    print("The candidate is eligible for admission.")
else:
    print("The candidate is not eligible for admission.")


