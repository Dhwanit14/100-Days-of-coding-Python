student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores :
    # print(grades)
    score = (student_scores[student])

    if student >= 91 and student <= 100 :
         student_grades[student] = "Outstanding"
    elif student >= 81 and student <= 90 :
         student_grades[student] = "Exceeds Expectations"
    elif student >= 71 and student <= 80 :
         student_grades[student] = "Acceptable"
    else :
         student_grades[student] = "Fail"       
        
print(student_grades)

