import random

all_grades = []
final_grades = []
big_grades = []


print("STUDENT GPA CALCULATOR")
print("-------------------------------------------------")
print()
print("Here are the students' grades before curving:") 
print()


def generate_students(students):
  for i in range(students):
    grade = random.randrange(0,41)/10
    print("Student ",(i+1), ": ", grade, sep ="")
    all_grades.append(grade)
  return all_grades


def get_curve(scores):
  for i in range(len(scores)):
    get_diff = 4.0 - (max(scores))
    round_diff = round(get_diff, 1)
  return round_diff


def large_scores(scores):
  big = max(scores)
  for i in range(len(scores)):
    if all_grades[i] == big:
      big_grades.append(i+1)
      for i in range(len(big_grades)):
        big_grades[i] = str(big_grades[i])
  return(", ".join(big_grades))


def curved_grades(extra):
  if extra > 0:
    print("\n\nHere are the students' grades after curving:")
    print("-------------------------------------------------")
    print()
    print("The curve was", extra, "GPA points.")
    print()
    for i in range(len(all_grades)):
      final_grades = round((all_grades[i] + extra), 1)
      print("Student",(i+1),"-->",final_grades,"(had", all_grades[i],"before)")
    print()
    if len(big_grades) == 1:
      print("Student", top_students, "had the highest GPA and set the curve.")
      print("-------------------------------------------------")
    if len(big_grades) >= 2:
      print("Students", top_students, "had the highest GPA and set the curve.")
      print("-------------------------------------------------")
  elif extra == 0:
    print()
    print("Highest score is equal to 4.0; curve is equal to 0.")



# -------MAIN-------

grades = generate_students(20)
curve = get_curve(grades)
top_students = large_scores(grades)
curved_grades(curve)
