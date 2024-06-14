amount=float(input('Enter the shopping amount: '))
mem_level=input('Enter the membership level(Regular or Gold): ')
#判斷輸入的會員等級是否正確
if mem_level!='Regular' and mem_level!='Gold':
	print('Invalid member level')
#判斷會員等級及他的購物金額可得到的折扣
if mem_level=='Regular':
	if amount<=1000:
		print(mem_level,amount)
	elif amount>1000 and amount<=2000:
		final_amount=amount*0.9
		print(mem_level,final_amount)
	elif amount>2000 and amount<=3000:
		final_amount=amount*0.85
		print(mem_level,final_amount)
	elif amount>3000:
		final_amount=amount*0.8
		print(mem_level,final_amount)
if mem_level=='Gold':
	if amount<=1000:
		print(mem_level,amount)
	elif amount>1000 and amount<=2000:
		final_amount=amount*0.85
		print(mem_level,final_amount)
	elif amount>2000 and amount<=3000:
		final_amount=amount*0.8
		print(mem_level,final_amount)
	elif amount>3000:
		final_amount=amount*0.75
		print(mem_level,final_amount)