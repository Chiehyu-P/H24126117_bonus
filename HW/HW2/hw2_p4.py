layers=int(input('Enter the number of layers(2 to 5)= '))
length=int(input('Enter the side length of the top layer= '))
growth=int(input('Enter the growth of each layers(2 to 5)= '))
width=int(input('Enter the trunk width(odd number, 3 to 9)= '))
height=int(input('Enter the trunk height(4 to 10)= '))

def large(l):	
	#印單行的空格和符號
	#l:那一個三角形的層數 i:第幾行
	for i in range(1,l+1):
		#只要不是第一個三角形且在第一行的時候就不用印那一行
		if l!=length and i==1:
			continue
		#印空格(第一行空格數等於最下面三角形的邊長-1)
		print((length+(layers-1)*growth-i)*' ',end='')
		#印符號
		for j in range(1,2*i):
			#每一行的符號個數=1+2(n-1)
			#每一行 頭or尾or最後一行 要印#
			if j==1 or j==2*i-1 or i==l:	
				print('#',end='')
			else:
				print('@',end='')
		print('\n',end='')

#k是從第一個三角形跑l有幾層在跑符號最後跑到第layers
for k in range(1,layers+1):
	large(length+(k-1)*growth)

#印樹幹
for i in range(1,height+1):
	print(int((length+(layers-1)*growth)-width/2)*' ',end='')
	print(width*'|')




 