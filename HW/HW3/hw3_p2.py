polynomial=input('Input polynomial: ')
var=int(input('Input the value of X: '))
Y= False
if polynomial[0]=='-':
	Y=True



def minus(operation):
	if len(operation)==3:
		if(operation[1]=='*'):
			return var*var
		else:
			return var**var
	if len(operation)==2:
		coef=operation[0].split('*')
		if coef[0]=='':
			coef1=1
		elif coef[0]=='-':
			coef1=-1
		else:
			coef1=coef[0]
		if operation[1]=='': # ''
			power1=1
			return int(coef1)*(var**int(power1))
		power=operation[1].split('^')	
		if power[1]=='': # '' 
			power1=var
		else:	
			power1=power[1] 
		return int(coef1)*(var**int(power1))

	
	elif len(operation)==1:
		if '*' in operation[0]:
			coef=operation[0].split('*')
			return int(coef[0])*var
		elif '^' in operation[0]:
			power=operation[0].split('^')
			if power[0]==' ':
				power1=var
				return var**int(power1)
			else:	
				power1=power[0]
				return var**int(power1)
		else:
			return int(operation[0])
ans=0
step_1=polynomial.split('+')
length1=len(step_1)
for i in range(0,length1):
	step_2=step_1[i].split('-')
	length2=len(step_2)
	for j in range(0,length2):
		operation=step_2[j].split('X')
		if j==0:
			if i==0 and Y==True:
				continue
				#ans-=minus(operation)
			else:
				ans+=minus(operation)
		else:
			ans-=minus(operation)

print('Evaluted Result:',ans)
	


# origin     2*X^4-X^3+17*X+9453
# step_1     [2*X^4-X^3]  [17*X]  [9453]

# step_2     [[2*X^4]  [X^3]]  [[17*X]]  [[9453]]
# operation  [2*,^4]  [^3]  [17*]  [9453]

# 沒有 有
# 沒有 沒有
# 有 有
# 有 沒有
# 常數


# origin     X^5-3*X+2
# step_1     [X^5-3*X]  [2] 

# step_2     [[X^5]  [3*X]]  [2]
# operation  [[''],[^5]] [[3*],['']]  [2]  

