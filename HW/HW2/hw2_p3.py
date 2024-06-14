year=int(input('Please input Year:'))
month=int(input('Please input Month:'))

#判斷閏年
def leapyear(y):
	if (y%4==0 and y%100!=0) or y%400==0:
		return True
	else:
		return False

#判斷第一天從禮拜幾開始
def date_start(y,m):
	if m==1 or m==2:
		y=y-1
	if m==2:
		m=12
	else:
		m=(m-2)%12
	d=10
	b=y%100
	a=y/100
	date=(d+int(2.6*m-0.2)-2*a+b+int(a/4)+int(b/4))%7
	return date

spaceCnt=int((date_start(year,month)-1))
#建立每個月的天數(2月有閏/平年)
array=[31,-1,31,30,31,30,31,31,30,31,30,31]
if leapyear(year)==True:
	array[1]=29
else:
	array[1]=28

print('Sun Mon Tue Wed Thu Fri Sat')
print(spaceCnt*'    ',end='')

for i in range(1,array[month-1]+1):
	if (i+spaceCnt)%7==0:
		if 1<=i<=9:
			print('0'+str(i))
		else:
			print(i)
	elif (i+spaceCnt)%7!=0:
		if 1<=i<=9:
			print('0'+str(i),end='  ')
		else:
			print(i,' ',end='')







