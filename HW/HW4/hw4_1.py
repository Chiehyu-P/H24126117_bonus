import random
import time

def mine(first_cell):
	mines=[]
	col=['a','b','c','d','e','f','g','h','i']
	rows=['1','2','3','4','5','6','7','8','9']
	while len(mines)<10:
		x,y=random.randint(0,8),random.randint(0,8)
		c,r=col[x],rows[y]
		if (c,r) not in mines and (c!=first_cell[0] and r!=first_cell[1]):
			mines.append((c,r))
	return mines

def display_board():
	print('    a     b     c     d     e     f     g     h     i')
	for i in range(9):
		print((' +'+' ---')*9+' +')
		print(str(i+1)+'|     '*10,end='\n')
	print((' +'+' ---')*9+' +')


def valid_cell(cell):
	col=['a','b','c','d','e','f','g','h','i']
	rows=['1','2','3','4','5','6','7','8','9']
	while True:
		column=cell[0]
		row=cell[1]
		if column not in col or row not in rows:
			print('Invalid cell. Enter the column followed by the row(ex: a5). To add or remove a flag, add \'f\' to the cell (ex: a5f).')
			continue
		else:
			return cell
			break


def mines_graph(mines):
	mines_list=[['0']*9 for i in range(9)]
	for i in mines:
		cell_1=ord(i[0])-96
		cell_2=int(i[1])
		mines_list[cell_2-1][cell_1-1]='X'
	return mines_list



display_board()
print('Enter the column followed by the row(ex: a5). To add or remove a flag, add \'f\' to the cell (ex: a5f). Type \'help\' to show this message again')
mines_left=10
cell_list=[]


first_cell=input('Enter the cell ({} mines left): '.format(mines_left))
if valid_cell(first_cell)!=False:
	cell_list=cell_list.append(valid_cell(first_cell))

	
mines=mine(first_cell)
mines_graph(mines)
print(mines)




while True:
	cell=input('Enter the cell ({} mines left): '.format(mines_left))
	if cell=='help':
		print('Enter the column followed by the row(ex: a5). To add or remove a flag, add \'f\' to the cell (ex: a5f). Type \'help\' to show this message again')
		continue
	elif valid_cell(cell)!=False:
		cell_list=cell_list.append(valid_cell(cell))		
	elif cell in cell_list:
		print('That cell is already shown')
		continue
	elif (cell[0],cell[1]) in mines:
		print('Game over')
		break
	
