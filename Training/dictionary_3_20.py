student_grades = [10,15,12,18,20]
print('Type = ',type(student_grades))

mysum = sum(student_grades)
print('mysum = ',mysum)
print('Average = ',(mysum/len(student_grades)))

student_grades = {'Ashok' : 9.1,'Sim' : 6.8,'Marry':5.1}
print('Type = ',type(student_grades))
#dir(dict)
#help(dict.values)
mysum = sum(student_grades.values())
print('mysum = ',mysum)
print('Average = ',(mysum/len(student_grades.values())))
print('Keys = ',student_grades.keys())