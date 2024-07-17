# fruits = ["apple" , "banana", "grapes"]

# for i in fruits :
#     print(i)


# function to calcualte the average height of the student using LISTS and FOR Loop :
# input for creating the list
student_heights = input("Input a list of student heights ").split(" ")

#creating the list
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#sum up the number int he list
sum = 0
for i in student_heights :
   sum = sum + i

#to calcualte the length of the list
number_of_students = 0 
for student in student_heights :
   number_of_students+=1
   print(number_of_students)

# for averageing the height
average_height = sum / number_of_students

#Finally printing the output
print(student_heights) 
print(f"Average of all student's height is {round(average_height)}")

