from ch2 import scoregrade as check_grade
point = input("点数を入力してください。　point = ")
point = int(point)

grade = check_grade(point)
print(grade)
