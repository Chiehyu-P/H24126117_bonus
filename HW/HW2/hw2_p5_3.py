num=int(input('The number of the requested element in Fibonacci(n)= '))
s1=input('The first string for Palindromic detection (s1)= ')
s2=input('The second string for Palindromic detection (s2)= ')
plaintext=input('The plaintext to be encrypted: ')
p_len=len(plaintext)

array=[0,1]
for i in range(2,num+1):
	fabo=array[i-2]+array[i-1]
	array.append(fabo)
print('The '+str(num)+'-th Fibonacci sequence number is:'+str(array[num]))
Fn=array[num]

def palindromic(string):
	length=len(string)
	t=[[0]*length for i in range(length)]

	tmp=0
	i=0
	j=0
	max_len=0
	maxi=0
	maxj=0

	while tmp<length:
		if j<length and i<length:
			if i==j:
				t[i][j]=1
			elif string[i]==string[j]:
				if t[i+1][j-1]!=0 or j-1<i+1:
					t[i][j]=2+t[i+1][j-1]
				elif t[i+1][j-1]==0:
					t[i][j]=0
			elif string[i]!=string[j]:
				t[i][j]=0
			if t[i][j]>max_len:
				max_len=t[i][j]
				maxi=i
				maxj=j
			j+=1
			i+=1
		else:
			tmp+=1
			i=0
			j=tmp
	print('Longest palindrome substring is: '+str(string[maxi:maxj+1]))
	print('Length is: '+str(max_len))
	return(max_len)



L1=palindromic(s1)
L2=palindromic(s2)
print('The encrypted text is: ',end='')
for i in range(0,p_len):
	output=L1*(ord(plaintext[i])+Fn)+L2
	output=((output-65)%26)+65
	print(str(chr(output)),end='')


