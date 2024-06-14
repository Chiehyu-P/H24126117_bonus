i=9
j=9
while j>=1:
	while i>=1:
		k=0
		while k>=-2:#在k=-3的時候跳出迴圈
			print(i,'X',(j+k),'=',(j+k)*i,end='\t')
			k-=1 #讓j每次都減一
		print()
		i-=1
	print()
	j=j-3 #j到下一層就減3
	i=9
		