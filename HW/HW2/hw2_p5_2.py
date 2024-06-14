string=input('Enter a string: ')
 	#   a b a d d a
 	# a 1 0 3 0 0 0
  	# b   1 0 0 0 0
 	# a     1 0 0 4
 	# d       1 2 0
	# d         1 0
 	# a           1

length=len(string)
#建立一個二維陣列長度(length*length)
t=[[0]*length for i in range(length)]

tmp=0
i=0
j=0
max_len=0
maxi=0
maxj=0

while tmp<length:
	if j<length and i<length:
		#如果i到j是同一個位置回文長度是1(t[i][j]=1)
		if i==j:
			t[i][j]=1
		#如果字串中位置i跟位置j的字一樣
		elif string[i]==string[j]:
			#判斷字串中位置[i+1]跟[j-1]是否有回文(t[i+1][j-1]!=0/==0)(之前判斷過)
			#j-1<i+1為i跟j是連續的情況
			if t[i+1][j-1]!=0 or j-1<i+1:
				#有回文 t[i][j]=2(string中[i]跟[j]的長度)+t[i+1][j-1](中間也是回文的長度)
				t[i][j]=2+t[i+1][j-1]
			#如果中間沒有回文 t[i][j]=0(字串位置i到j就沒有回文)
			elif t[i+1][j-1]==0:
				t[i][j]=0
		elif string[i]!=string[j]:
			t[i][j]=0
		#找到陣列中最長的長度
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
