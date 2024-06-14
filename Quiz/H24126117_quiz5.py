time=True

size=int(input('Enter the size of the grid: '))
#印出(size*size)的圖形
graph=[['_']*size for i in range(size)]
for row in graph:
	print(' '.join(row))

#重複執行直到'done'
while time==True:
	cell=input('Enter the cell coordinates to edit: ')
	if cell=='done':
		exit()
	value=input('Enter the new value for the cell: ')
	#分割cell的逗號
	cell_list=cell.split(',')
	row=int(cell_list[0])
	col=int(cell_list[1])
	#更改圖形內的值
	for space in cell_list:
		graph[row][col]=value
	#印出新圖形
	for row in graph:
		print(' '.join(row))

