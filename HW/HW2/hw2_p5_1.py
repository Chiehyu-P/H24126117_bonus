num=int(input('Input an integer number: '))
array=[0,1]
for i in range(2,num+1):
	fibo=array[i-2]+array[i-1]
	array.append(fibo)
print('The '+str(num)+'-th Fibonacci sequence number is:'+str(array[num]))