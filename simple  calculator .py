# STUDENT MARKS , PERCENTAGE , GRADE AND ACADEMIC PERFORMANCE
name = input("enter student name:")
n = int(input("enter number of subjects:"))
total = 0
for i in range(1,n+1):
    mark = float(input(f"enter mark for subject{i}:"))
    total += mark
percentage = total/n
if percentage >= 90:
    grade ="A+"
    performance = "outstanding"
elif percentage >= 80:
    grade = "A"
    performance = "execellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage >= 60:
    grade = "c"
    performance = "Good"
elif percentage >= 50:
    grade = "D"
    performance = "Average"
else:
    grade = "F"
    performance = "needs improvement"
print("\n --- academic performance----")
print("student name", name)
print("total marks", mark)
print("percentage", percentage)
print("grade :", grade)
print("performance", performance)

