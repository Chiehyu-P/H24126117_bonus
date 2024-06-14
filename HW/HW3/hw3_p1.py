num=int(input('Input the total number of students(n>0): '))
last_student=list(range(1,num+1))
index=0

#continue until the list remains one student
while len(last_student)>1:
	index=(index+2)%len(last_student)
	#remove students from the list
	last_student.pop(index)

print('The last ID is: '+str(last_student[0]))