range_num=int(input('input a range number: '))
factor=[]
perfect_num=[]

for i in range(2,range_num+1):
	for j in range(1,i+1):
		#找i的所有因數
		if i%j==0:
			factor.append(j)
	if sum(factor)-i==i:  #determine whether the number is perfect number or not
		perfect_num.append(i)
	#下一個迴圈要先把上一個i的因數清除
	factor.clear()

print('Perfect numbers:')
for i in range(len(perfect_num)):
	print(perfect_num[i])


# range_num=int(input('input a range number: '))
# factor=[]
# perfect_num=''

# for i in range(2,range_num+1):
# 	for j in range(1,i+1):
# 		#找i的所有因數
# 		if i%j==0:
# 			factor.append(j)
# 	if sum(factor)-i==i:  #determine whether the number is perfect number or not
# 		perfect_num=perfect_num+str(i)+' '
# 	#下一個迴圈要先把上一個i的因數清除
# 	factor.clear()

# print('Perfect numbers:'+perfect_num)



